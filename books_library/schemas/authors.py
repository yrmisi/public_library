from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

FirstName = Annotated[str, Field(min_length=1, max_length=150)]
LastPatronymicName = Annotated[str, Field(min_length=1, max_length=256)]


class AuthorBase(BaseModel):
    """Base class schema author."""

    first_name: FirstName
    patronymic_name: LastPatronymicName | None = None
    last_name: LastPatronymicName


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

    first_name: FirstName | None = None
    last_name: LastPatronymicName | None = None
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
