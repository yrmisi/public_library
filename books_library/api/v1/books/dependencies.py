from typing import Annotated
from uuid import UUID

from fastapi import Depends

from database.models import Book
from dependencies.session import AsyncSessionDep
from schemas import BookCreate, BookUpdate

from ..authors.dependencies import AuthorRepositoryDep
from .repositories import BookRepository
from .services import BookService


def repository_provider_dependency(session: AsyncSessionDep) -> BookRepository:
    return BookRepository(session)


BookRepositoryDep = Annotated[BookRepository, Depends(repository_provider_dependency)]


def book_service_dependency(
    book_repo: BookRepositoryDep,
    author_repo: AuthorRepositoryDep,
) -> BookService:
    return BookService(book_repo, author_repo)


BookServiceDep = Annotated[BookService, Depends(book_service_dependency)]


async def create_book_dependency(
    book_create: BookCreate,
    book_service: BookServiceDep,
) -> Book:
    return await book_service.create_book(book_create=book_create)


BookCreateDep = Annotated[Book, Depends(create_book_dependency)]


async def get_books_list_dependency(book_service: BookServiceDep) -> list[Book]:
    return await book_service.get_books_list()


BooksListDep = Annotated[list[Book], Depends(get_books_list_dependency)]


async def get_book_by_id_dependency(
    book_id: UUID,
    book_service: BookServiceDep,
) -> Book:
    return await book_service.get_book_by_id(book_id=book_id)


BookIDDep = Annotated[Book, Depends(get_book_by_id_dependency)]


async def update_book_dependency(
    book_id: UUID,
    book_update: BookUpdate,
    book_service: BookServiceDep,
) -> Book:
    return await book_service.update_book(book_id=book_id, book_update=book_update)


BookUpdateDep = Annotated[Book, Depends(update_book_dependency)]
