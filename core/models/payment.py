from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func, Float, ForeignKey

from . import User
from .base import Base


class Payment(Base):
    payment_id: Mapped[str] = mapped_column(String, unique=True)
    subscribe: Mapped[str]

    time_of_action: Mapped[datetime] = mapped_column(DateTime)
    price: Mapped[float] = mapped_column(Float)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
