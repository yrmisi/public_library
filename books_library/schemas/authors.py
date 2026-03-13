from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    """Base class schema author."""

    first_name: str
    patronymic_name: str | None = None
    last_name: str


class AuthorCreate(AuthorBase):
    """Creating an author."""

    pass


class AuthorRead(AuthorBase):
    """Read the author."""

    id: UUID
    is_deleted: bool
    updated_at: datetime | None = None
    created_at: datetime


class AuthorUpdate(BaseModel):
    """Updating the author."""

    first_name: str | None = None
    last_name: str | None = None
    is_deleted: bool | None = None

    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "first_name": "String",
                    "patronymic_name": "String",
                    "last_name": "String",
                    "is_deleted": False,
                },
            ]
        },
    )
