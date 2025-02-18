from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MinLen, MaxLen


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    login: str
    telegram_id: int


class Register(BaseModel):
    login: Annotated[str, MinLen(3), MaxLen(30)] | None
    password: Annotated[str, MinLen(3), MaxLen(30)] | None
    telegram_id: int | None


class Login(BaseModel):
    login: Annotated[str, MinLen(3), MaxLen(30)]
    password: Annotated[str, MinLen(3), MaxLen(30)]


class UserUpdate(UserBase):
    login: str | None = None
    telegram_id: int | None = None
