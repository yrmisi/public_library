from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .author import Author


class Book(Base):
    """Model Book."""

    author_id: Mapped[UUID] = mapped_column(
        ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(
        Text,
        default="title",
        server_default="title",
        nullable=False,
        index=True,
    )
    short_description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    pub_date: Mapped[date]

    author: Mapped["Author"] = relationship(
        "Author",
        back_populates="books",
        lazy="joined",
    )
