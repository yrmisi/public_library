from datetime import date
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Book
from schemas import BookCreate


class BookRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list(self) -> list[Book]:
        stmt = select(Book).order_by(Book.id)
        books = await self.session.scalars(stmt)

        return list(books.all())

    async def get_by_id(self, book_id: UUID) -> Book | None:
        return await self.session.get(Book, book_id)

    async def create(self, book_create: BookCreate) -> Book:
        book = Book(**book_create.model_dump())

        self.session.add(book)
        await self.session.commit()

        return book

    async def update(
        self,
        book: Book,
        update_data: dict[str, str | date],
    ) -> None:
        for key, val in update_data.items():
            setattr(book, key, val)

        await self.session.commit()
        await self.session.refresh(book)
