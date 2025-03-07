from .schemas import ArticleCreate, ArticleBase, ArticleUpdate
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Article


async def get_all_articles(session: AsyncSession) -> list[Article]:
    stmt = select(Article).order_by(Article.id)
    result: Result = await session.execute(stmt)
    articles = result.scalars().all()
    return list(articles)


async def create_article(session: AsyncSession, article_in: ArticleBase) -> Article:
    user = Article(**article_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def article_by_id(session: AsyncSession, article_id) -> Article | None:
    return await session.get(Article, article_id)


async def update_article(
    session: AsyncSession,
    article: Article,
    article_update: ArticleUpdate,
) -> Article:
    for name, value in article_update.model_dump(exclude_none=True).items():
        setattr(article, name, value)
    await session.commit()

    return article


async def delete_article(
    session: AsyncSession,
    article: Article,
) -> None:
    await session.delete(article)
    await session.commit()
