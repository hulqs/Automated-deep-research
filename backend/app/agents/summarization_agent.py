"""
Agent 3: Content Summarization.
"""
import logging
from langchain_core.prompts import ChatPromptTemplate
from app.agents.base import BaseAgent

logger = logging.getLogger(__name__)

SUMMARIZATION_SYSTEM = """You are an expert academic summarizer. Your role is to:
1. Synthesize search results into coherent summaries
2. Extract key facts, arguments, and findings
3. Identify contradictions or gaps in the collected information
4. Structure knowledge into organized nodes

Always cite sources when presenting facts. Be precise and academic in tone.
If the input materials are in Chinese, summarize in Chinese."""

MAX_INPUT_LENGTH = 15000


class SummarizationAgent(BaseAgent):
    """Agent 3: Content Summarization -- synthesizes findings, builds knowledge nodes."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

    async def summarize_round(
        self, topic: str, results: list[dict], round_num: int
    ) -> dict:
        results_text = []
        for i, r in enumerate(results[:30]):
            snippet = r.get("snippet", "")[:800]
            results_text.append(
                f"[{i + 1}] Source: {r.get('source', '?')} | Title: {r.get('title', '')}\n{snippet}"
            )
        combined = "\n---\n".join(results_text)[:12000]

        logger.info(
            f"Summarization round {round_num}: input length = {len(combined)} chars"
        )

        enhanced_system = (
            f"{SUMMARIZATION_SYSTEM}\n\n"
            "CRITICAL JSON RULES:\n"
            "1. Output ONLY the JSON object, no explanations, no markdown, no code blocks\n"
            "2. Ensure all double quotes inside strings are escaped with backslash\n"
            "3. Do not add trailing commas at the end of arrays or objects\n"
            "4. All fields must be present exactly as specified\n"
            "5. confidence must be a float between 0 and 1"
        )

        user_prompt = f"""Topic: {topic}
Round: {round_num}
Collected materials:
{combined}

Create a round summary. Return ONLY valid JSON with no extra text:
{{
    "round_summary": "synthesized text in markdown (in Chinese if input is Chinese)",
    "key_findings": ["finding 1", "finding 2"],
    "knowledge_nodes": [
        {{ "title": "...", "content": "...", "node_type": "concept|fact|reference", "confidence": 0.0-1.0 }}
    ],
    "remaining_questions": ["question 1"]
}}"""

        return await self.call_llm_json(enhanced_system, user_prompt)

    async def final_summary(self, topic: str, all_rounds: list[dict]) -> str:
        rounds_text = []
        for rd in all_rounds:
            rounds_text.append(
                f"Round {rd.get('round', '?')}: {rd.get('round_summary', '')[:2000]}"
            )

        user_prompt = (
            f"Topic: {topic}\n"
            f"Research rounds:\n"
            f"{'\\n=== ROUND ===\\n'.join(rounds_text)[:8000]}\n\n"
            "Produce a comprehensive academic summary in Markdown format with sections:"
            "\n## 概述\n## 核心发现\n## 不同观点\n## 知识空白\n## 参考文献\n"
            "Write in Chinese if the topic and materials are in Chinese."
        )

        return await self.call_llm(SUMMARIZATION_SYSTEM, user_prompt)
