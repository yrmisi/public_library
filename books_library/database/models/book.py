from datetime import date

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Book(Base):
    """Model Book."""

    title: Mapped[str] = mapped_column(
        Text,
        default="title",
        server_default="title",
        nullable=False,
        index=True,
    )
    pub_date: Mapped[date]
