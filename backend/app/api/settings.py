"""
User Settings API endpoints.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User
from app.core.security import get_current_user
from app.schemas.settings import UserSettingsUpdate, UserSettingsResponse
from app.services.settings_service import SettingsService

router = APIRouter(prefix="/api/settings", tags=["Settings"])


@router.get("", response_model=UserSettingsResponse)
async def get_settings(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get current user's API settings."""
    return await SettingsService.get_settings(db, current_user)


@router.put("", response_model=UserSettingsResponse)
async def update_settings(
    data: UserSettingsUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create or update user's API settings."""
    return await SettingsService.update_settings(db, current_user, data)


