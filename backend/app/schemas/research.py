from datetime import datetime
from pydantic import BaseModel, Field, model_validator
import enum
from typing import Optional, List, Any

class ResearchTaskCreate(BaseModel):
    title: str = Field(..., max_length=300)
    topic: str = Field(..., min_length=10)
    description: str = Field(default="", max_length=2000)

class ResearchQuery(BaseModel):
    query: str
    source: str = "web"
    lang: str = "zh"

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str
    source: str
    relevance_score: float = 0.0

class KnowledgeGap(BaseModel):
    topic: str
    reason: str
    suggested_queries: List[str] = []

class TodoItemCreate(BaseModel):
    content: str
    priority: str = "medium"
    order_index: int = 0

class TodoItemResponse(BaseModel):
    id: str
    content: str
    is_completed: bool
    priority: str
    order_index: int

    class Config:
        from_attributes = True

class IntermediateReportResponse(BaseModel):
    id: str
    round_number: int
    content: str
    gaps_identified: List[dict]
    created_at: datetime

    class Config:
        from_attributes = True

class ResearchTaskResponse(BaseModel):
    id: str
    title: str
    topic: str
    description: str
    status: str
    progress: float
    queries: List[dict]
    search_results: List[dict]
    knowledge_gaps: List[dict]
    summary: str
    final_report: str
    report_path: str
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    todo_items: list = []
    intermediate_reports: list = []

    class Config:
        from_attributes = True

    @model_validator(mode="before")
    @classmethod
    def extract_fields(cls, data: Any) -> Any:
        """Convert ORM object to dict, skipping unloaded relationships."""
        if hasattr(data, "__dict__") and not isinstance(data, dict):
            result = {}
            for col in data.__table__.columns:
                val = getattr(data, col.key)
                if isinstance(val, enum.Enum):
                    val = val.value
                result[col.key] = val
            # Safely get relationships
            for rel_name in ("todo_items", "intermediate_reports"):
                try:
                    rel_val = getattr(data, rel_name, None)
                    if rel_val is not None and hasattr(rel_val, "__iter__"):
                        result[rel_name] = list(rel_val)
                except Exception:
                    result[rel_name] = []
            return result
        return data

class ResearchTaskListResponse(BaseModel):
    tasks: List[ResearchTaskResponse]
    total: int