from typing import Annotated
from uuid import UUID

from fastapi import Depends

from database.models import Book
from dependencies.session import AsyncSessionDep
from exceptions import BookNotFoundError
from schemas import BookCreate

from .repositories import BookRepository


def repository_provider(session: AsyncSessionDep) -> BookRepository:
    return BookRepository(session)


RepositoryDep = Annotated[BookRepository, Depends(repository_provider)]


async def create_book(book_create: BookCreate, repo: RepositoryDep) -> Book:
    return await repo.create(book_create=book_create)


BookCreateDep = Annotated[Book, Depends(create_book)]


async def get_books_list(book_repo: RepositoryDep) -> list[Book]:
    return await book_repo.list()


BooksListDep = Annotated[list[Book], Depends(get_books_list)]


async def get_book_by_id(book_id: UUID, book_repo: RepositoryDep) -> Book:
    book = await book_repo.get_by_id(book_id=book_id)
    if book is not None:
        return book
    raise BookNotFoundError(
        book_id=book_id,
    )


BookIDDep = Annotated[Book, Depends(get_book_by_id)]
