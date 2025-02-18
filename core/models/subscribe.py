from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float

from .base import Base


class Subscribe(Base):
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)

    message_count: Mapped[int] = mapped_column(Integer, default=30)
    max_length_sym: Mapped[int] = mapped_column(Integer, default=1200)
    image_count: Mapped[int] = mapped_column(Integer, default=0)
    voice_count: Mapped[int] = mapped_column(Integer, default=0)
