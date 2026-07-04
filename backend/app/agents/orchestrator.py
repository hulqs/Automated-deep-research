import logging
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.research_task import ResearchTask, TaskStatus
from app.models.article import TodoItem, IntermediateReport
from app.agents.decomposition_agent import DecompositionAgent
from app.agents.search_agent import SearchAgent
from app.agents.summarization_agent import SummarizationAgent
from app.agents.report_agent import ReportAgent
from app.agents.todo_planner_agent import TodoPlannerAgent
from app.agents.image_agent import ImageAgent

logger = logging.getLogger(__name__)

MAX_ROUNDS = 3

class ResearchOrchestrator:
    """
    指挥所有 AI 代理按顺序执行任务
    """
    def __init__(
        self,
        db: AsyncSession,
        task: ResearchTask,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
    ):
        self.db = db
        self.task = task
        self.decomposer = DecompositionAgent(api_key=api_key, base_url=base_url, model=model)
        self.searcher = SearchAgent(api_key=api_key, base_url=base_url, model=model)
        self.summarizer = SummarizationAgent(api_key=api_key, base_url=base_url, model=model)
        self.reporter = ReportAgent(api_key=api_key, base_url=base_url, model=model)
        self.planner = TodoPlannerAgent(api_key=api_key, base_url=base_url, model=model)
        self.image_agent = ImageAgent(api_key=api_key, base_url=base_url, model=model)

    async def run(self) -> ResearchTask:
        # Phase 1: 提取关键词
        await self._update_status(TaskStatus.DECOMPOSING, 0.05)
        if await self._is_cancelled():
            return self.task
        decomposition = await self.decomposer.decompose(self.task.topic, self.task.description)
        all_queries = []
        for sq in decomposition.get("sub_questions", []):
            all_queries.extend(sq.get("queries", []))
        self.task.queries = all_queries
        await self.db.commit()

        # Phase 2: 分轮次搜索
        all_results = []
        round_summaries = []
        all_gaps = []

        for round_num in range(1, MAX_ROUNDS + 1):
            if await self._is_cancelled():
                return self.task
            progress = 0.05 + (round_num / MAX_ROUNDS) * 0.40
            await self._update_status(TaskStatus.SEARCHING, progress)

            round_data = await self.searcher.search_round(all_queries, round_num)
            all_results.extend(round_data["results"])

            # Evaluate completeness
            eval_result = await self.searcher.evaluate_completeness(
                self.task.topic, all_results, all_queries
            )
            gaps = eval_result.get("knowledge_gaps", [])
            all_gaps.extend(gaps)

            # Summarize this round
            await self._update_status(TaskStatus.SUMMARIZING, progress + 0.05)
            summary = await self.summarizer.summarize_round(
                self.task.topic, round_data["results"], round_num
            )
            round_summaries.append(summary)

            # Save intermediate report
            ir = IntermediateReport(
                task_id=self.task.id,
                round_number=round_num,
                content=summary.get("round_summary", ""),
                gaps_identified=gaps,
            )
            self.db.add(ir)

            self.task.search_results = all_results[:50]
            self.task.knowledge_gaps = all_gaps[:20]
            await self.db.commit()

            if eval_result.get("is_sufficient") or round_num >= MAX_ROUNDS:
                break

        if await self._is_cancelled():
            return self.task

        # Phase 3: 生成最终摘要
        await self._update_status(TaskStatus.SUMMARIZING, 0.75)
        final_summary = await self.summarizer.final_summary(
            self.task.topic, round_summaries
        )
        self.task.summary = final_summary

        if await self._is_cancelled():
            return self.task

        # Phase 4: 生成 TODO 待办计划
        todo_plan = await self.planner.generate_plan_with_evaluation(self.task.topic, self.task.description, final_summary, all_gaps)
        for phase in todo_plan.get("phases", []):
            for t in phase.get("todos", []):
                item = TodoItem(
                    task_id=self.task.id,
                    content=f"[{phase['phase']}] {t['content']}",
                    priority=t.get("priority", "medium"),
                    order_index=t.get("order_index", 0),
                )
                self.db.add(item)
        await self.db.commit()

        if await self._is_cancelled():
            return self.task

        # Phase 5: 生成报告
        await self._update_status(TaskStatus.GENERATING, 0.85)
        knowledge_nodes = []
        for rs in round_summaries:
            knowledge_nodes.extend(rs.get("knowledge_nodes", []))

        final_report = await self.reporter.generate_report(
            self.task.topic, final_summary, all_results, knowledge_nodes,
            [{"content": t.get("content"), "is_completed": False}
             for phase in todo_plan.get("phases", [])
             for t in phase.get("todos", [])],
        )

        # Phase 6: 图像增强 -- 仅在源材料包含图片时才添加
        await self._update_status(TaskStatus.GENERATING, 0.92)
        key_concepts = decomposition.get("key_concepts", [])
        try:
            placements = await self.image_agent.identify_image_placements(
                self.task.topic, final_report, key_concepts,
                search_results=all_results,  # 传入源材料，让 LLM 判断是否有真实图片
            )
            if placements:
                enriched = await self.image_agent.fetch_images_for_placements(placements)
                if enriched:
                    final_report = await self.image_agent.embed_images_in_report(
                        final_report, enriched
                    )
                    logger.info(
                        f"Enhanced report with {len(enriched)} images "
                        f"(from {len(placements)} candidate placements) for task {self.task.id}"
                    )
                else:
                    logger.info(
                        f"No images found for any of the {len(placements)} placements. "
                        f"Report kept without images for task {self.task.id}"
                    )
            else:
                logger.info(
                    f"No valid image placements identified (no source materials "
                    f"contain images). Report kept without images for task {self.task.id}"
                )
        except Exception as e:
            logger.warning(f"Image enhancement skipped (non-critical): {e}")

        self.task.final_report = final_report
        self.task.status = TaskStatus.COMPLETED
        self.task.progress = 1.0
        self.task.completed_at = datetime.now(timezone.utc)
        await self.db.commit()

        return self.task

    async def _update_status(self, status: TaskStatus, progress: float):
        self.task.status = status
        self.task.progress = min(progress, 1.0)
        await self.db.commit()

    async def _is_cancelled(self) -> bool:
        """Check if the task has been cancelled externally (status set to FAILED)."""
        await self.db.refresh(self.task)
        if self.task.status == TaskStatus.FAILED:
            logger.info(f"Task {self.task.id} was cancelled by user")
            return True
        return False
