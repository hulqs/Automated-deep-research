"""
Base agent using LangChain ChatOpenAI with robust JSON handling.
"""
import json
import logging
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from app.config import setting
from json_repair import repair_json
from tenacity import stop_after_attempt, wait_exponential, retry

logger = logging.getLogger(__name__)


class BaseAgent:
    """Base agent with LangChain ChatOpenAI and robust JSON handling.

    Accepts optional api_key, base_url, model to allow per-user configuration.
    Falls back to global settings if not provided.
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
    ):
        self._api_key = api_key or setting.OPENAI_API_KEY
        self._base_url = base_url or setting.OPENAI_BASE_URL
        self._model = model or setting.OPENAI_MODEL

        self.llm = ChatOpenAI(
            api_key=self._api_key,
            base_url=self._base_url,
            model=self._model,
            temperature=0.3,
            max_tokens=4000,
            timeout=120.0,
        )
        self.llm_json = ChatOpenAI(
            api_key=self._api_key,
            base_url=self._base_url,
            model=self._model,
            temperature=0.2,
            max_tokens=8192,
            timeout=120.0,
            model_kwargs={"response_format": {"type": "json_object"}},
        )
        self.model = self._model

    async def call_llm(
        self, system_prompt: str, user_prompt: str, temperature: float = 0.3
    ) -> str:
        """Call the LLM with system and user prompts, return text response."""
        try:
            llm = self.llm
            if temperature != 0.3:
                llm = ChatOpenAI(
                    api_key=self._api_key,
                    base_url=self._base_url,
                    model=self._model,
                    temperature=temperature,
                    max_tokens=4000,
                    timeout=120.0,
                )
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt),
            ]
            respondes = await llm.ainvoke(messages)
            content = respondes.content
            if isinstance(content, list):
                content = "".join(
                    block.get("text", "") if isinstance(block, dict) else str(block)
                    for block in content
                )
            return content or ""
        except Exception as e:
            logger.error(f"LLM call failed: {str(e)}", exc_info=True)
            raise RuntimeError(f"LLM call failed: {e}") from e

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def call_llm_json(
        self, system_prompt: str, user_prompt: str, temperature: float = 0.2
    ) -> dict:
        """
        Robust JSON call with LangChain JSON mode and automatic repair.
        """
        try:
            enhanced_system = (
                f"{system_prompt}\n\n"
                "CRITICAL INSTRUCTIONS:\n"
                "1. Respond ONLY with a valid JSON object, no other text, explanations, or markdown.\n"
                "2. Do NOT wrap the JSON in code blocks (```json ... ```).\n"
                "3. Ensure all strings are properly closed and quotes are escaped.\n"
                "4. Do not add trailing commas at the end of arrays or objects.\n"
                "5. If you cannot generate valid JSON, return an empty object: {}"
            )

            llm = self.llm_json
            if temperature != 0.2:
                llm = ChatOpenAI(
                    api_key=self._api_key,
                    base_url=self._base_url,
                    model=self._model,
                    temperature=temperature,
                    max_tokens=8192,
                    timeout=120.0,
                    model_kwargs={"response_format": {"type": "json_object"}},
                )

            messages = [
                SystemMessage(content=enhanced_system),
                HumanMessage(content=user_prompt),
            ]
            resp = await llm.ainvoke(messages)

            raw_content = resp.content
            if isinstance(raw_content, list):
                raw_content = "".join(
                    block.get("text", "") if isinstance(block, dict) else str(block)
                    for block in raw_content
                )
            raw_content = raw_content or "{}"

            logger.debug(f"Raw LLM JSON output: {raw_content[:500]}...")

            # Layer 1: standard JSON parse
            try:
                return json.loads(raw_content)
            except json.JSONDecodeError as e:
                logger.warning(f"Standard JSON parse failed: {e}. Attempting repair...")

            # Layer 2: json-repair
            try:
                repaired = repair_json(raw_content)
                result = json.loads(repaired)
                logger.info("JSON repair successful")
                return result
            except Exception as e2:
                logger.error(f"JSON repair failed: {e2}")
                logger.error(f"Original content: {raw_content}")
                raise RuntimeError(
                    "LLM returned invalid JSON that could not be repaired"
                ) from e2

        except Exception as e:
            logger.error(f"LLM JSON call failed: {str(e)}", exc_info=True)
            raise RuntimeError(f"LLM JSON call failed: {e}") from e
