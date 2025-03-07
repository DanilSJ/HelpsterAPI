from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Blog

from . import crud


async def dep_blog_by_id(
    blog_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Blog:
    blog = await crud.blog_by_id(session=session, blog_id=blog_id)
    if blog is not None:
        return blog

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Blog {blog_id} not found",
    )
