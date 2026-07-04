"""
Agent 1: Problem Decomposition using LangChain prompt templates.
"""
from langchain_core.prompts import ChatPromptTemplate
from app.agents.base import BaseAgent

DECOMPOSITION_SYSTEM = """You are an expert research planner. Your task is to decompose a broad research topic into specific, searchable queries.

For the given research topic, you should:
1. Break it down into 3-7 focused sub-questions
2. For each sub-question, generate 1-3 concrete search queries
3. Suggest which sources to search (wikipedia, arxiv, web)
4. Identify key concepts and terminology

If the input is in Chinese, respond with Chinese sub-questions and queries.
If the input is in English, respond in English.

Output your analysis as a structured plan with queries ready for execution."""

DECOMPOSITION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", DECOMPOSITION_SYSTEM),
    ("human", """Research Topic: {topic}
Description: {description}

Please decompose this topic and return a JSON object with this structure:
{{
    "sub_questions": [
        {{
            "question": "...",
            "keywords": ["..."],
            "queries": [
                {{ "query": "...", "source": "wikipedia|arxiv|web", "lang": "zh|en" }}
            ]
        }}
    ],
    "key_concepts": ["concept1", "concept2"],
    "suggested_depth": "basic|moderate|deep",
    "domain": "subject area"
}}"""),
])


class DecompositionAgent(BaseAgent):
    """Agent 1: Problem Decomposition -- breaks open topics into searchable queries."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

    async def decompose(self, topic: str, description: str = "") -> dict:
        messages = DECOMPOSITION_PROMPT.format_messages(
            topic=topic, description=description or "N/A"
        )
        system = messages[0].content
        user = messages[1].content
        return await self.call_llm_json(str(system), str(user))
