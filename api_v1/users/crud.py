from api_v1.users.schemas import Register, UserUpdate
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User


async def create_user(session: AsyncSession, user_in: Register) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession, user_id) -> User | None:
    return await session.get(User, user_id)


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate,
) -> object:
    for name, value in user_update.model_dump(exclude_none=True).items():
        setattr(user, name, value)
    await session.commit()

    user = {
        "login": user.login,
        "telegram_id": user.telegram_id,
    }

    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
    await session.commit()
