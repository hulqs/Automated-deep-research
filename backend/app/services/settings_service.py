import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.user_settings import UserSettings
from app.models.user import User
from app.schemas.settings import UserSettingsCreate, UserSettingsUpdate
from app.agents.base import BaseAgent

logger = logging.getLogger(__name__)


class SettingsService:
    @staticmethod
    async def get_settings(db: AsyncSession, user: User) -> UserSettings:
        result = await db.execute(
            select(UserSettings).where(UserSettings.user_id == user.id)
        )
        settings = result.scalar_one_or_none()
        if not settings:
            # Create default settings
            settings = UserSettings(user_id=user.id)
            db.add(settings)
            await db.commit()
            await db.refresh(settings)
        return settings

    @staticmethod
    async def update_settings(
        db: AsyncSession, user: User, data: UserSettingsUpdate
    ) -> UserSettings:
        result = await db.execute(
            select(UserSettings).where(UserSettings.user_id == user.id)
        )
        settings = result.scalar_one_or_none()

        if not settings:
            settings = UserSettings(user_id=user.id)
            db.add(settings)

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(settings, key, value)

        await db.commit()
        await db.refresh(settings)
        return settings

    @staticmethod
    async def test_connection(
        api_key: str,
        base_url: str,
        model: str,
    ) -> dict:
        """
        Test the API connection by making a lightweight LLM call.
        Returns {"ok": True, "message": "..."} on success,
        or {"ok": False, "message": "..."} on failure.
        """
        from app.config import setting as global_setting

        test_key = api_key or global_setting.OPENAI_API_KEY
        test_url = base_url or global_setting.OPENAI_BASE_URL
        test_model = model or global_setting.OPENAI_MODEL

        try:
            agent = BaseAgent(api_key=test_key, base_url=test_url, model=test_model)
            result = await agent.call_llm(
                system_prompt="You are a helpful assistant. Respond with exactly 'OK' and nothing else.",
                user_prompt="Say OK",
                temperature=0.0,
            )
            if "OK" in result or "ok" in result.lower():
                return {
                    "ok": True,
                    "message": f"连接成功！模型 '{test_model}' 响应正常。",
                }
            return {
                "ok": True,
                "message": f"连接成功，但模型 '{test_model}' 响应异常: {result[:200]}",
            }
        except Exception as e:
            logger.warning(f"Settings connection test failed: {e}")
            return {
                "ok": False,
                "message": f"连接失败: {str(e)}",
            }
