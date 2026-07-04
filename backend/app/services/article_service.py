from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.article import Article, ArticleStatus, KnowledgeNode
from app.models.user import User
from app.schemas.article import ArticleCreate, ArticleUpdate

class ArticleService:
    @staticmethod
    async def create_article(db: AsyncSession, user: User, data: ArticleCreate) -> Article:
        article = Article(
            user_id=user.id,
            title=data.title,
            content=data.content,
            abstract=data.abstract,
            keywords=data.keywords,
            source_url=data.source_url,
            source_type=data.source_type,
            word_count=str(len(data.content.split())) if data.content else "0",
        )
        db.add(article)
        await db.commit()
        await db.refresh(article)
        return article

    @staticmethod
    async def list_articles(db: AsyncSession, user: User, skip: int = 0, limit: int = 20):
        result = await db.execute(
            select(Article)
            .where(Article.user_id == user.id)
            .order_by(Article.updated_at.desc())
            .offset(skip)
            .limit(limit)
        )
        articles = result.scalars().all()
        count_result = await db.execute(select(Article).where(Article.user_id == user.id))
        total = len(count_result.scalars().all())
        return articles, total

    @staticmethod
    async def get_article(db: AsyncSession, user: User, article_id: str) -> Article:
        result = await db.execute(
            select(Article).where(Article.id == article_id, Article.user_id == user.id)
        )
        article = result.scalar_one_or_none()
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        return article

    @staticmethod
    async def update_article(db: AsyncSession, user: User, article_id: str, data: ArticleUpdate) -> Article:
        article = await ArticleService.get_article(db, user, article_id)
        if data.title is not None:
            article.title = data.title
        if data.content is not None:
            article.content = data.content
            article.word_count = str(len(data.content.split()))
        if data.abstract is not None:
            article.abstract = data.abstract
        if data.keywords is not None:
            article.keywords = data.keywords
        if data.status is not None:
            article.status = ArticleStatus(data.status)
        await db.commit()
        await db.refresh(article)
        return article

    @staticmethod
    async def delete_article(db: AsyncSession, user: User, article_id: str):
        article = await ArticleService.get_article(db, user, article_id)
        await db.delete(article)
        await db.commit()

    @staticmethod
    async def create_knowledge_node(
        db: AsyncSession, user: User, task_id: str | None, title: str, content: str,
        node_type: str = "concept", source: str = "", confidence: float = 0.5
    ) -> KnowledgeNode:
        node = KnowledgeNode(
            user_id=user.id,
            task_id=task_id,
            title=title,
            content=content,
            node_type=node_type,
            source=source,
            confidence=str(confidence),
        )
        db.add(node)
        await db.commit()
        await db.refresh(node)
        return node

    @staticmethod
    async def list_knowledge_nodes(db: AsyncSession, user: User, task_id: str | None = None):
        stmt = select(KnowledgeNode).where(KnowledgeNode.user_id == user.id)
        if task_id:
            stmt = stmt.where(KnowledgeNode.task_id == task_id)
        stmt = stmt.order_by(KnowledgeNode.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()
