from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from core.models import db_helper
from .crud import get_all_blogs
from .schemas import BlogBase, BlogUpdate
from . import crud
from .dependencies import dep_blog_by_id

router = APIRouter(tags=["blogs"])


@router.get("/", response_model=list[BlogBase])
async def get_blog(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_all_blogs(session)


@router.get("/{blog_id}/", response_model=BlogBase)
async def get_blog_by_id(
    blog: BlogBase = Depends(dep_blog_by_id),
):
    return blog


@router.post("/", response_model=BlogBase)
async def create_blog(
    blog_in: BlogBase,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_blog(
        session=session,
        blog_in=blog_in,
    )


@router.patch("/{blog_id}/")
async def update_blog(
    blog_update: BlogUpdate,
    blog: BlogBase = Depends(dep_blog_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_blog(
        session=session,
        blog=blog,
        blog_update=blog_update,
    )


@router.delete("/{blog_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(
    blog: BlogBase = Depends(dep_blog_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_blog(
        session=session,
        blog=blog,
    )
