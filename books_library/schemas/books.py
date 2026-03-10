from datetime import date
from typing import Annotated
from uuid import UUID, uuid7

from pydantic import BaseModel, ConfigDict, Field

Title = Annotated[str, Field(min_length=1, max_length=500)]


class BookBase(BaseModel):
    """Base class schema."""

    author_id: UUID
    title: str
    pub_date: date
    short_description: Title | None = None


class BookCreate(BookBase):
    """Create a new book."""

    title: Title


class BookRead(BookBase):
    """Read a book."""

    id: UUID


class BookUpdate(BookBase):
    """Update a book."""

    author_id: UUID | None = None
    title: Title | None = None
    pub_date: date | None = None

    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "author_id": str(uuid7()),
                    "title": "String",
                    "pub_date": date(2026, 3, 9).isoformat(),
                    "short_description": "String",
                },
            ]
        },
    )
