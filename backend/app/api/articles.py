from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User
from app.core.security import get_current_user
from app.schemas.article import ArticleCreate, ArticleUpdate, ArticleResponse, KnowledgeNodeCreate, KnowledgeNodeResponse
from app.services.article_service import ArticleService

router = APIRouter(prefix="/api/articles", tags=["Articles"])

@router.post("/", response_model=ArticleResponse)
async def create_article(
    data: ArticleCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await ArticleService.create_article(db, current_user, data)

@router.get("/", response_model=list[ArticleResponse])
async def list_articles(
    skip: int = 0,
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    articles, _ = await ArticleService.list_articles(db, current_user, skip, limit)
    return articles

@router.get("/{article_id}", response_model=ArticleResponse)
async def get_article(
    article_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await ArticleService.get_article(db, current_user, article_id)

@router.put("/{article_id}", response_model=ArticleResponse)
async def update_article(
    article_id: str,
    data: ArticleUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await ArticleService.update_article(db, current_user, article_id, data)

@router.delete("/{article_id}")
async def delete_article(
    article_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await ArticleService.delete_article(db, current_user, article_id)
    return {"detail": "Article deleted"}

@router.post("/knowledge-nodes", response_model=KnowledgeNodeResponse)
async def create_knowledge_node(
    data: KnowledgeNodeCreate,
    task_id: str | None = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await ArticleService.create_knowledge_node(
        db, current_user, task_id, data.title, data.content,
        data.node_type, data.source, data.confidence,
    )

@router.get("/knowledge-nodes", response_model=list[KnowledgeNodeResponse])
async def list_knowledge_nodes(
    task_id: str | None = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await ArticleService.list_knowledge_nodes(db, current_user, task_id)
