from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ArticleCreate(BaseModel):
    title: str = Field(..., max_length=300)
    content: str = Field(default="")
    abstract: str = Field(default="")
    keywords: List[str] = Field(default_factory=list)
    source_url: str = Field(default="")
    source_type: str = Field(default="manual")

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    abstract: Optional[str] = None
    keywords: Optional[List[str]] = None
    status: Optional[str] = None

class ArticleResponse(BaseModel):
    id: str
    title: str
    content: str
    abstract: str
    keywords: List[str]
    status: str
    source_url: str
    source_type: str
    word_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class KnowledgeNodeCreate(BaseModel):
    title: str
    content: str
    node_type: str = "concept"
    source: str = ""
    confidence: float = 0.5

class KnowledgeNodeResponse(BaseModel):
    id: str
    title: str
    content: str
    node_type: str
    source: str
    confidence: float
    created_at: datetime

    class Config:
        from_attributes = True
