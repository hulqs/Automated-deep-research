"""
AI API endpoints for natural language input parsing.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel, Field
from app.database import get_db
from app.models.user import User
from app.models.user_settings import UserSettings
from app.core.security import get_current_user
from app.services.ai_service import AIService

router = APIRouter(prefix="/api/ai", tags=["AI"])


class NaturalInputRequest(BaseModel):
    text: str = Field(..., min_length=3, max_length=2000, description="Natural language input describing what the user wants")


class NaturalInputResponse(BaseModel):
    action: str
    payload: dict
    explanation: str


@router.post("/parse-input", response_model=NaturalInputResponse)
async def parse_natural_input(
    data: NaturalInputRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Parse natural language input to determine whether to create a research task or article."""
    # Load user API settings
    result = await db.execute(
        select(UserSettings).where(UserSettings.user_id == current_user.id)
    )
    us = result.scalar_one_or_none()
    api_key = us.openai_api_key if us and us.openai_api_key else None
    base_url = us.openai_base_url if us else None
    model = us.openai_model if us else None

    service = AIService(api_key=api_key, base_url=base_url, model=model)
    result_ai = await service.parse_natural_input(data.text)
    return result_ai
