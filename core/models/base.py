from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from datetime import datetime
from sqlalchemy import DateTime, func


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)

    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # Database-side default
        default=datetime.utcnow,  # Python-side default
    )
