from datetime import date
from typing import Annotated, Any
from uuid import UUID, uuid7

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

MAX_LENGTH = 500
SUFFIX = "..."

TitleShortDescType = Annotated[str, Field(min_length=1, max_length=MAX_LENGTH)]
VolumesCountType = Annotated[int, Field(ge=1, le=100)]


class BookBase(BaseModel):
    """Base class schema."""

    author_id: UUID
    title: TitleShortDescType
    pub_date: date
    short_description: TitleShortDescType | None = None
    volumes_count: VolumesCountType | None = None

    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "author_id": str(uuid7()),
                    "title": "String",
                    "pub_date": date(2026, 3, 9).isoformat(),
                    "short_description": "String",
                    "volumes_count": 1,
                },
            ]
        },
    )

    @field_validator("pub_date", mode="before")
    @classmethod
    def val_pub_date(cls, val: Any) -> date:
        if isinstance(val, str):
            try:
                parsed_date = date.fromisoformat(val)
            except ValueError:
                raise ValidationError("Invalid date format. Use YYYY-MM-DD")
        elif isinstance(val, date):
            parsed_date = val
        else:
            raise ValidationError("Field - pub_date must be string in YYYY-MM-DD or date object")

        if parsed_date and parsed_date > date.today():
            raise ValidationError("The date cannot be in the future")

        return parsed_date

    @field_validator("short_description", mode="before")
    @classmethod
    def val_short_description(cls, val: Any) -> str:
        if not isinstance(val, str):
            raise ValidationError("Field - short_description must be a string.")

        if len(val) <= MAX_LENGTH:
            return val

        trim_length: int = MAX_LENGTH - len(SUFFIX)
        truncated: str = val[:trim_length]

        last_space: int = truncated.rfind(" ")
        truncated: str = truncated[:last_space]

        return truncated + SUFFIX


class BookCreate(BookBase):
    """Create a new book."""

    pass


class BookRead(BookBase):
    """Read a book."""

    id: UUID

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": str(uuid7()),
                    "author_id": str(uuid7()),
                    "title": "String",
                    "pub_date": date(2026, 3, 9).isoformat(),
                    "short_description": "String",
                    "volumes_count": 1,
                }
            ]
        }
    )


class BookUpdate(BookBase):
    """Update a book."""

    author_id: UUID | None = None
    title: TitleShortDescType | None = None
    pub_date: date | None = None
    short_description: TitleShortDescType | None = None
    volumes_count: VolumesCountType | None = None
