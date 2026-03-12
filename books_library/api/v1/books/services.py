from datetime import date
from uuid import UUID

from database.models import Author, Book
from exceptions import AuthorNotFoundError, BookNotFoundError
from schemas import BookCreate, BookUpdate

from ..authors.repositories import AuthorRepository
from .repositories import BookRepository


class BookService:
    def __init__(
        self,
        book_repo: BookRepository,
        author_repo: AuthorRepository,
    ) -> None:
        self.book_repo = book_repo
        self.author_repo = author_repo

    async def create_book(
        self,
        book_create: BookCreate,
    ) -> Book:
        author: Author | None = await self.author_repo.get_by_id(author_id=book_create.author_id)
        if author is None:
            raise AuthorNotFoundError(author_id=book_create.author_id)

        return await self.book_repo.create(book_create=book_create)

    async def get_books_list(self) -> list[Book]:
        return await self.book_repo.list()

    async def get_book_by_id(self, book_id: UUID) -> Book:
        book = await self.book_repo.get_by_id(book_id=book_id)
        if book is not None:
            return book
        raise BookNotFoundError(
            book_id=book_id,
        )

    async def update_book(
        self,
        book_id: UUID,
        book_update: BookUpdate,
    ) -> Book:
        book: Book | None = await self.book_repo.get_by_id(book_id=book_id)

        if book is None:
            raise BookNotFoundError(book_id=book_id)

        update_data: dict[str, str | date] = book_update.model_dump(exclude_unset=True)

        await self.book_repo.update(book, update_data)

        return book
