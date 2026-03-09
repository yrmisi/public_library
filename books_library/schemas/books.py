from datetime import date
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

Title = Annotated[str, Field(min_length=1, max_length=500)]


class BookBase(BaseModel):
    """Base class schema."""

    title: str
    pub_date: date


class BookCreate(BookBase):
    """Create a new book."""

    title: Title


class BookRead(BookBase):
    """Read a book."""

    id: UUID


class BookUpdate(BookBase):
    """Update a book."""

    title: Title | None = None
    pub_date: date | None = None

    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "title": "String",
                    "pub_date": date(2026, 3, 9).isoformat(),
                },
            ]
        },
    )
