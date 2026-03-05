from typing import Annotated
from uuid import UUID

from fastapi import Depends

from database.models import Book
from dependencies.session import AsyncSessionDp
from schemas import BookCreate

from .exceptions import BookNotFoundError
from .repositories import BookRepository


def repository_provider(session: AsyncSessionDp) -> BookRepository:
    return BookRepository(session)


RepositoryDp = Annotated[BookRepository, Depends(repository_provider)]


async def create_book(book_create: BookCreate, repo: RepositoryDp) -> Book:
    return await repo.create(book_create=book_create)


BookCreateDp = Annotated[Book, Depends(create_book)]


async def get_books_list(book_repo: RepositoryDp) -> list[Book]:
    return await book_repo.list()


BooksListDp = Annotated[list[Book], Depends(get_books_list)]


async def get_book_by_id(book_id: UUID, book_repo: RepositoryDp) -> Book:
    book = await book_repo.get_by_id(book_id=book_id)
    if book is not None:
        return book
    raise BookNotFoundError(
        book_id=book_id,
    )


BookIDDp = Annotated[Book, Depends(get_book_by_id)]
