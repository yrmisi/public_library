from uuid import UUID

from fastapi import status


class libraryBaseError(Exception):
    pass


class BookNotFoundError(libraryBaseError):
    def __init__(
        self,
        book_id: UUID,
        detail: str = "Book not found, ID - {book_id}",
        status_code: int = status.HTTP_404_NOT_FOUND,
    ) -> None:
        self.book_id = book_id
        self.detail = detail
        self.status_code = status_code
        super().__init__(self.detail)
