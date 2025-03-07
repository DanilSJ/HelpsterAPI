from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from core.models import db_helper, article
from .crud import get_all_articles
from .schemas import ArticleBase, ArticleUpdate
from . import crud
from .dependencies import dep_article_by_id

router = APIRouter(tags=["articles"])


@router.get("/", response_model=list[ArticleBase])
async def get_articles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_all_articles(session)


@router.get("/{blog_id}/", response_model=ArticleBase)
async def get_article_by_id(
    article: ArticleBase = Depends(dep_article_by_id),
):
    return article


@router.post("/", response_model=ArticleBase)
async def create_blog(
    article_in: ArticleBase,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_article(
        session=session,
        article_in=article_in,
    )


@router.patch("/{article_id}/")
async def update_article(
    article_update: ArticleUpdate,
    article: ArticleBase = Depends(dep_article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_article(
        session=session,
        article=article,
        article_update=article_update,
    )


@router.delete("/{article_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    article: ArticleBase = Depends(dep_article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_article(
        session=session,
        article=article,
    )
