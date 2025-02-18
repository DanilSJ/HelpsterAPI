from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Integer, func
from .base import Base


class User(Base):
    telegram_id: Mapped[int]

    login: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    password: Mapped[str]
    admin = Mapped[bool]

    prefix: Mapped[str] = mapped_column(
        String,
        default="",
        server_default="",
    )

    ai_model: Mapped[str] = mapped_column(
        String,
        default="gpt-3.5-turbo",
        server_default="gpt-3.5-turbo",
    )
    voice_model: Mapped[str] = mapped_column(
        String,
        default="pNInz6obpgDQGcFmaJgB",
        server_default="pNInz6obpgDQGcFmaJgB",
    )

    message_count: Mapped[int] = mapped_column(Integer, default=30)
    max_length_sym: Mapped[int] = mapped_column(Integer, default=1200)
    image_count: Mapped[int] = mapped_column(Integer, default=0)
    voice_count: Mapped[int] = mapped_column(Integer, default=0)
