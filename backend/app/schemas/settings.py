from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserSettingsCreate(BaseModel):
    openai_api_key: str = Field(default="", max_length=500)
    openai_base_url: str = Field(default="https://api.deepseek.com", max_length=500)
    openai_model: str = Field(default="gpt-4o", max_length=100)


class UserSettingsUpdate(BaseModel):
    openai_api_key: Optional[str] = Field(default=None, max_length=500)
    openai_base_url: Optional[str] = Field(default=None, max_length=500)
    openai_model: Optional[str] = Field(default=None, max_length=100)


class UserSettingsResponse(BaseModel):
    id: str
    user_id: str
    openai_api_key: str
    openai_base_url: str
    openai_model: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
