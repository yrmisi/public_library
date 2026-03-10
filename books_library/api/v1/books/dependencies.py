from datetime import date
from typing import Annotated
from uuid import UUID

from fastapi import Depends

from database.models import Author, Book
from dependencies.session import AsyncSessionDep
from exceptions import AuthorNotFoundError, BookNotFoundError
from schemas import BookCreate, BookUpdate

from ..authors.dependencies import AuthorRepositoryDep
from .repositories import BookRepository


def repository_provider(session: AsyncSessionDep) -> BookRepository:
    return BookRepository(session)


BookRepositoryDep = Annotated[BookRepository, Depends(repository_provider)]


async def create_book(
    book_create: BookCreate,
    book_repo: BookRepositoryDep,
    author_repo: AuthorRepositoryDep,
) -> Book:
    author: Author | None = await author_repo.get_by_id(author_id=book_create.author_id)
    if author is None:
        raise AuthorNotFoundError(author_id=book_create.author_id)

    return await book_repo.create(book_create=book_create)


BookCreateDep = Annotated[Book, Depends(create_book)]


async def get_books_list(book_repo: BookRepositoryDep) -> list[Book]:
    return await book_repo.list()


BooksListDep = Annotated[list[Book], Depends(get_books_list)]


async def get_book_by_id(book_id: UUID, book_repo: BookRepositoryDep) -> Book:
    book = await book_repo.get_by_id(book_id=book_id)
    if book is not None:
        return book
    raise BookNotFoundError(
        book_id=book_id,
    )


BookIDDep = Annotated[Book, Depends(get_book_by_id)]


async def update_book(
    book_id: UUID,
    book_update: BookUpdate,
    book_repo: BookRepositoryDep,
) -> Book:
    book: Book | None = await book_repo.get_by_id(book_id=book_id)

    if book is None:
        raise BookNotFoundError(book_id=book_id)

    update_data: dict[str, str | date] = book_update.model_dump(exclude_unset=True)

    for key, val in update_data.items():
        setattr(book, key, val)

    await book_repo.session.commit()
    await book_repo.session.refresh(book)

    return book


BookUpdateDep = Annotated[Book, Depends(update_book)]
