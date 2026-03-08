from uuid import UUID

from fastapi import status

from .base import libraryBaseError


class AuthorNotFoundError(libraryBaseError):
    def __init__(
        self,
        author_id: UUID,
        detail: str = "Author not found, ID - {author_id}",
        status_code: int = status.HTTP_404_NOT_FOUND,
    ) -> None:
        self.author_id = author_id
        self.detail = detail.format(author_id=self.author_id)
        self.status_code = status_code
        super().__init__(self.detail, self.status_code)
