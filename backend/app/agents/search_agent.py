"""
Agent 2: Multi-round Search using LangChain.
"""
from langchain_core.prompts import ChatPromptTemplate
from app.agents.base import BaseAgent
from app.tools import SearchAggregator

SEARCH_SYSTEM = """You are a research search coordinator. Your role is to:
1. Execute search queries across multiple sources
2. Evaluate if enough information has been gathered
3. Identify knowledge gaps that need further searching
4. Decide whether to continue or stop searching

You analyze search results and determine if more rounds are needed."""

EVALUATE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", SEARCH_SYSTEM),
    ("human", """Topic: {topic}
Search results so far ({result_count} items):
{results_summary}

Queries used so far:
{queries_used}

Evaluate whether more searching is needed. Return JSON:
{{
    "is_sufficient": true/false,
    "knowledge_gaps": [
        {{ "topic": "...", "reason": "...", "suggested_queries": ["query1"] }}
    ],
    "confidence": 0.0-1.0
}}"""),
])


class SearchAgent(BaseAgent):
    """Agent 2: Multi-round Search -- collects info across sources, identifies gaps."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

    async def search_round(self, queries: list[dict], round_num: int = 1) -> dict:
        all_results = []
        for q in queries:
            source_list = [q.get("source", "web")]
            results = await SearchAggregator.search(q["query"], source_list)
            for r in results:
                r["query"] = q["query"]
            all_results.extend(results)

        return {
            "round": round_num,
            "results": all_results,
            "result_count": len(all_results),
        }

    async def evaluate_completeness(
        self, topic: str, results: list[dict], queries_used: list[dict]
    ) -> dict:
        results_summary = []
        for r in results[:20]:
            results_summary.append({
                "title": r.get("title", ""),
                "snippet": (r.get("snippet", "") or "")[:200],
                "source": r.get("source", ""),
            })

        messages = EVALUATE_PROMPT.format_messages(
            topic=topic,
            result_count=len(results),
            results_summary=str(results_summary),
            queries_used=str(queries_used),
        )
        return await self.call_llm_json(
            str(messages[0].content), str(messages[1].content)
        )
