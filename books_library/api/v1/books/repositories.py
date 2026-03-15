from datetime import date
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database.models import Book
from schemas import BookCreate


class BookRepository:
    """Data access layer for Book entities."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize the BookRepository with a database session."""
        self.session = session

    async def list(self) -> list[Book]:
        """Return all books ordered by ID, eagerly loading related author."""
        stmt = select(Book).options(selectinload(Book.author)).order_by(Book.id)
        books = await self.session.scalars(stmt)

        return list(books.all())

    async def get_by_id(self, book_id: UUID) -> Book | None:
        """Return a book by ID or None if it does not exist."""
        return await self.session.get(Book, book_id)

    async def create(self, book_create: BookCreate) -> Book:
        """Create and persist a new book entity."""
        book = Book(**book_create.model_dump())

        self.session.add(book)
        await self.session.commit()

        return book

    async def update(
        self,
        book: Book,
        update_data: dict[str, str | date],
    ) -> None:
        """Apply partial updates to a book and sync changes to the database."""
        for key, val in update_data.items():
            setattr(book, key, val)

        await self.session.commit()
        await self.session.refresh(book)
