from fastapi import APIRouter
from users.schemas import Register
from users import crud

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}/")
def get_user(user_id: int):
    return crud.get_user(user_id)


@router.post("/")
def create_user(user: Register):
    return crud.create_user(user)
