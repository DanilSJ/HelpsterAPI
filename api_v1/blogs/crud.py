from .schemas import BlogCreate, BlogUpdate, BlogBase
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Blog


async def get_all_blogs(session: AsyncSession) -> list[Blog]:
    stmt = select(Blog).order_by(Blog.id)
    result: Result = await session.execute(stmt)
    blogs = result.scalars().all()
    return list(blogs)


async def create_blog(session: AsyncSession, blog_in: BlogBase) -> Blog:
    user = Blog(**blog_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def blog_by_id(session: AsyncSession, blog_id) -> Blog | None:
    return await session.get(Blog, blog_id)


async def update_blog(
    session: AsyncSession,
    blog: Blog,
    blog_update: BlogUpdate,
) -> Blog:
    for name, value in blog_update.model_dump(exclude_none=True).items():
        setattr(blog, name, value)
    await session.commit()

    return blog


async def delete_blog(
    session: AsyncSession,
    blog: Blog,
) -> None:
    await session.delete(blog)
    await session.commit()
