from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.user_settings import UserSettings
from app.models.user import User
from app.schemas.settings import UserSettingsCreate, UserSettingsUpdate


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
