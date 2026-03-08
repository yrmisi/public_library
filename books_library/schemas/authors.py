from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


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
