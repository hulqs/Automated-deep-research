"""
AI Service for parsing natural language input into research tasks or articles.
Uses LangChain for intelligent intent classification and field extraction.
"""
import logging
from app.agents.base import BaseAgent

logger = logging.getLogger(__name__)

PARSE_SYSTEM_PROMPT = """You are an intelligent assistant that analyzes user input and determines whether 
they want to start a research task or create an article.

Classification rules:
- If the user wants to RESEARCH, INVESTIGATE, STUDY, EXPLORE, SEARCH for information, 
  or mentions keywords like "研究", "调查", "探索", "分析", "查一下", "了解", "调研" -- it's a research task.
- If the user wants to WRITE, CREATE, DRAFT, COMPOSE an article, essay, report, or blog post,
  or mentions keywords like "写", "撰写", "创作", "编写", "文章", "报告", "博客" -- it's an article.
- If the user gives a topic without clear intent, default to research (they probably want to learn first).

For research tasks, extract:
- title: A concise 5-15 word title summarizing the research topic
- topic: The detailed research topic/question (at least 20 characters, more detailed than the title)
- description: Any additional context, constraints, or focus areas

For articles, extract:
- title: A concise article title
- content: Leave empty (user will fill in)
- abstract: A one-sentence preview of what the article will cover
- keywords: 3-5 relevant keywords

IMPORTANT: Always respond in the same language as the user's input.
If the input is in Chinese, all output fields should be in Chinese."""


class AIService:
    """Service for AI-powered input parsing and intent classification."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        self.agent = BaseAgent(api_key=api_key, base_url=base_url, model=model)

    async def parse_natural_input(self, text: str) -> dict:
        """
        Parse natural language input and return structured intent.
        Returns a dict with action ("research" or "article"), payload, and explanation.
        """
        user_prompt = f"""User input: {text}

Analyze this input and return a JSON object:

{{
    "action": "research" or "article",
    "payload": {{
        // For research:
        "title": "extracted/created title",
        "topic": "detailed research topic",
        "description": "additional context or empty string",
        
        // For article:
        "title": "article title",
        "content": "",
        "abstract": "brief one-sentence preview",
        "keywords": ["keyword1", "keyword2", "keyword3"]
    }},
    "explanation": "One sentence explaining what you will do, in the user's language"
}}

Important:
1. Only include fields relevant to the chosen action (research or article)
2. For research, topic must be detailed and at least 20 characters
3. For articles, keywords should be an array of 3-5 strings
4. explanation should tell the user what kind of task you are creating and why"""

        try:
            result = await self.agent.call_llm_json(PARSE_SYSTEM_PROMPT, user_prompt, temperature=0.3)
            action = result.get("action", "research")
            payload = result.get("payload", {})

            # Validate and normalize
            if action not in ("research", "article"):
                action = "research"

            if action == "research":
                if not payload.get("title"):
                    payload["title"] = text[:50]
                if not payload.get("topic") or len(payload.get("topic", "")) < 10:
                    payload["topic"] = text
                if "description" not in payload:
                    payload["description"] = ""
                # Remove article-only fields
                payload.pop("content", None)
                payload.pop("abstract", None)
                payload.pop("keywords", None)
            else:
                if not payload.get("title"):
                    payload["title"] = text[:50]
                if "content" not in payload:
                    payload["content"] = ""
                if "abstract" not in payload:
                    payload["abstract"] = ""
                if "keywords" not in payload or not isinstance(payload.get("keywords"), list):
                    payload["keywords"] = []
                # Remove research-only fields
                payload.pop("topic", None)
                payload.pop("description", None)

            return {
                "action": action,
                "payload": payload,
                "explanation": result.get("explanation", f"正在创建{'研究任务' if action == 'research' else '文章'}..."),
            }
        except Exception as e:
            logger.error(f"AI parse failed: {e}, falling back to research")
            return {
                "action": "research",
                "payload": {
                    "title": text[:50],
                    "topic": text,
                    "description": "",
                },
                "explanation": "已自动创建研究任务（AI分析失败，使用默认设置）",
            }
