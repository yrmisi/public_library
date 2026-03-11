from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .book import Book


class Author(Base):
    """The model describes data about the author."""

    __table_args__ = (
        UniqueConstraint(
            "first_name",
            "patronymic_name",
            "last_name",
            name="uq_author_full_name",
        ),
    )
    first_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )
    patronymic_name: Mapped[str | None] = mapped_column(
        String(256),
        nullable=True,
    )
    last_name: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        index=True,
    )
    is_deleted: Mapped[bool] = mapped_column(
        default=False,
        index=True,
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )

    books: Mapped[list["Book"]] = relationship(
        "Book",
        back_populates="author",
        lazy="selectin",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        """Displays the author's installation data."""
        return f"<Author(id={self.id}, name={self.full_name})>"

    @property
    def full_name(self) -> str:
        """Creates the author's full name."""
        parts_name: list[str] = [self.first_name, self.last_name]

        if self.patronymic_name:
            parts_name.insert(1, self.patronymic_name)

        return " ".join(parts_name)
