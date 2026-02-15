from typing import Annotated

from database import Book
from dependencies.session import AsyncSessionDp
from fastapi import Depends

from .repositories import BookRepository


def repository_provider(session: AsyncSessionDp) -> BookRepository:
    return BookRepository(session)


RepositoryDp = Annotated[BookRepository, Depends(repository_provider)]


async def get_books_list(book_repo: RepositoryDp) -> list[Book]:
    return await book_repo.list()


BooksListDp = Annotated[list[Book], Depends(get_books_list)]
