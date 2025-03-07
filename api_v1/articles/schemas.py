from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MinLen, MaxLen


class ArticleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    text: str
    img: str
    link: str


class ArticleCreate(ArticleBase):
    article_in: int


class ArticleUpdate(ArticleBase):
    title: str | None = None
    text: str | None = None
    img: str | None = None
    link: str | None = None
