"""
User Settings API endpoints.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, Field
from app.database import get_db
from app.models.user import User
from app.core.security import get_current_user
from app.schemas.settings import UserSettingsUpdate, UserSettingsResponse
from app.services.settings_service import SettingsService

router = APIRouter(prefix="/api/settings", tags=["Settings"])


class SettingsTestRequest(BaseModel):
    openai_api_key: str = Field(default="", max_length=500)
    openai_base_url: str = Field(default="", max_length=500)
    openai_model: str = Field(default="", max_length=100)


class SettingsTestResponse(BaseModel):
    ok: bool
    message: str


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


@router.post("/test", response_model=SettingsTestResponse)
async def test_settings(
    data: SettingsTestRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Test the API connection with the given settings before saving."""
    return await SettingsService.test_connection(
        api_key=data.openai_api_key,
        base_url=data.openai_base_url,
        model=data.openai_model,
    )


