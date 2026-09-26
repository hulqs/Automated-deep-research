"""
Agent 5: TODO Planner using LangChain.
"""
import json
from app.agents.base import BaseAgent

PLANNER_SYSTEM = """You are an academic research planner. Given a research topic and findings,
generate a structured TODO plan that a scholar can follow to deepen their research.

Include:
- Literature review tasks
- Experiment/analysis tasks
- Writing tasks
- Verification tasks

Each task should have a priority (high/medium/low) and logical ordering.
If the input is in Chinese, output the plan in Chinese."""

EVALUATOR_SYSTEM = """You are an academic research quality evaluator. Your job is to evaluate
whether a generated research TODO plan aligns with the user's research topic and requirements.

Evaluate the plan on these criteria:
1. Topic relevance: Do the planned tasks directly address the core research topic?
2. Requirement coverage: Does the plan cover the user's stated research description/goals?
3. Structural completeness: Does the plan include literature review, analysis, writing, and verification?
4. Logical coherence: Are tasks ordered sensibly and do phases build on each other?

Return a JSON object with:
- is_matching: true if the plan is well-aligned, false if it needs revision
- score: a number 1-10 rating the plan quality
- feedback: specific suggestions for improvement (empty string if is_matching is true)
- issues: a list of specific problems found (empty if is_matching is true)

Be strict but fair. A score of 7 or above should be considered matching.
If the input is in Chinese, output your response in Chinese."""

MAX_PLAN_RETRIES = 2


class TodoPlannerAgent(BaseAgent):
    """Agent 5: TODO Planner -- generates structured academic research plans."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

    async def generate_plan(
        self, topic: str, summary: str, gaps: list[dict], feedback: str = ""
    ) -> dict:
        gaps_text = []
        for g in (gaps or [])[:10]:
             gaps_text.append(
                f"- Gap: {g.get('topic', '')} -- {g.get('reason', '')}"
            )

        feedback_section = ""
        if feedback:
            feedback_section = f"""
CRITICAL FEEDBACK -- The previous plan had these issues, please fix them:
{feedback}
"""

        user_prompt = f"""Topic: {topic}
Research Summary: {summary[:2000]}
Knowledge Gaps:
{chr(10).join(gaps_text)[:1000]}
{feedback_section}
Generate a research TODO plan. Return JSON:
{{
    "plan_title": "Research Plan: {topic}",
    "phases": [
        {{
            "phase": "Phase name",
            "todos": [
                {{
                    "content": "specific task",
                    "priority": "high|medium|low",
                    "order_index": 0
                }}
            ]
        }}
    ]
}}"""

        return await self.call_llm_json(PLANNER_SYSTEM, user_prompt)

    async def evaluate_plan(
        self, topic: str, description: str, plan: dict
    ) -> dict:
        """Evaluate whether the generated plan matches the user's topic and needs.

        Returns a dict with is_matching (bool), score (int), feedback (str), issues (list).
        """
        plan_text = json.dumps(plan, ensure_ascii=False, indent=2)

        user_prompt = f"""User's Research Topic: {topic}
User's Research Description / Goals: {description or 'Not specified'}

Generated Research Plan:
{plan_text[:3000]}

Please evaluate whether this plan matches the user's topic and requirements."""

        result = await self.call_llm_json(EVALUATOR_SYSTEM, user_prompt)

        # Normalize: ensure sensible defaults for missing fields
        if "is_matching" not in result:
            score = result.get("score", 5)
            result["is_matching"] = score >= 7
        if "feedback" not in result:
            result["feedback"] = ""
        if "issues" not in result:
            result["issues"] = []
        if "score" not in result:
            result["score"] = 5

        return result

    async def generate_plan_with_evaluation(
        self, topic: str, description: str, summary: str, gaps: list[dict]
    ) -> dict:
        """Generate a research plan and evaluate it against user needs.

        If the plan doesn't match, regenerate with feedback up to MAX_PLAN_RETRIES times.
        Returns the final plan dict.
        """
        plan = await self.generate_plan(topic, summary, gaps)

        for attempt in range(MAX_PLAN_RETRIES + 1):
            evaluation = await self.evaluate_plan(topic, description, plan)

            if evaluation.get("is_matching"):
                return plan

            # Plan doesn't match -- regenerate with feedback
            feedback = evaluation.get("feedback", "")
            issues = evaluation.get("issues", [])
            combined_feedback = feedback
            if issues:
                combined_feedback = feedback + "\nSpecific issues:\n" + "\n".join(
                    f"- {issue}" for issue in issues
                )

            if attempt < MAX_PLAN_RETRIES:
                plan = await self.generate_plan(topic, summary, gaps, feedback=combined_feedback)

        return plan
