"""
Agent 4: Report Generation using LangChain.
"""
from langchain_core.prompts import ChatPromptTemplate
from app.agents.base import BaseAgent

REPORT_SYSTEM = """You are a senior academic report writer. Generate well-structured, citation-rich Markdown reports.

Guidelines:
- Use proper academic formatting with clear sections
- Include an abstract, introduction, body, conclusion, and references
- Cite all sources inline
- Maintain scholarly tone
- Use Markdown: headings, lists, blockquotes, tables where appropriate
- If the topic and materials are in Chinese, write the report in Chinese."""


class ReportAgent(BaseAgent):
    """Agent 4: Report Generation -- produces final structured Markdown reports."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

    async def generate_report(
        self,
        topic: str,
        summary: str,
        search_results: list[dict],
        knowledge_nodes: list[dict],
        todo_plan: list[dict] = None,
    ) -> str:
        sources_text = []
        seen = set()
        for r in search_results[:30]:
            url = r.get("url", "")
            if url and url not in seen:
                seen.add(url)
                sources_text.append(
                    f"- [{r.get('title', 'Untitled')}]({url}) -- {r.get('source', 'web')}"
                )

        nodes_text = []
        for n in (knowledge_nodes or [])[:20]:
            nodes_text.append(
                f"**{n.get('title', '')}** ({n.get('node_type', 'concept')}, "
                f"confidence: {n.get('confidence', '?')})\n{n.get('content', '')[:300]}"
            )

        todo_text = ""
        if todo_plan:
            todo_lines = []
            for t in todo_plan[:15]:
                checked = "x" if t.get("is_completed") else " "
                todo_lines.append(f"- [{checked}] {t.get('content', '')}")
            todo_text = "\n".join(todo_lines)

        user_prompt = f"""Topic: {topic}

Research Summary:
{summary[:3000]}

Knowledge Nodes:
{chr(10).join(nodes_text)[:2000]}

Sources:
{chr(10).join(sources_text)[:2000]}

TODO Plan:
{todo_text[:1000]}

Generate a complete academic research report in Markdown with:
# {topic}
## 摘要 (Abstract)
## 1. 引言 (Introduction)
## 2. 研究现状 (Literature Review)
## 3. 核心分析 (Analysis)
## 4. 研究发现 (Findings)
## 5. 研究规划与待办 (Research Plan)
## 6. 结论 (Conclusion)
## 参考文献 (References)

Write in Chinese if the topic is Chinese."""

        return await self.call_llm(REPORT_SYSTEM, user_prompt, temperature=0.4)
