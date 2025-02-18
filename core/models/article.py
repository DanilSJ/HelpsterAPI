from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Text

from .base import Base


class Article(Base):
    title: Mapped[str] = mapped_column(String)

    text: Mapped[str] = mapped_column(Text)
    img: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)
