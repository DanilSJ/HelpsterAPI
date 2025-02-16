from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen


class Register(BaseModel):
    login: Annotated[str, MinLen(3), MaxLen(30)] | None
    password: Annotated[str, MinLen(3), MaxLen(30)] | None
    telegram_id: int | None


class Login(BaseModel):
    login: Annotated[str, MinLen(3), MaxLen(30)]
    password: Annotated[str, MinLen(3), MaxLen(30)]


class UpdateUser(BaseModel):
    surname: str
