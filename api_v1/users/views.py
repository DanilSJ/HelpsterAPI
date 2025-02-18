from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import Register, UserBase, UserUpdate
from . import crud
from .dependencies import user_by_id

router = APIRouter(tags=["users"])


@router.get("/{user_id}/", response_model=UserBase)
async def get_user(
    user: UserBase = Depends(user_by_id),
):
    return user


@router.post("/", response_model=UserBase)
async def create_user(
    user_in: Register,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(session=session, user_in=user_in)


@router.patch("/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user: UserBase = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: UserBase = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_user(session=session, user=user)
