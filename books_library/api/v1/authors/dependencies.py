from typing import Annotated
from uuid import UUID

from fastapi import Depends

from database.models import Author
from dependencies.session import AsyncSessionDep
from schemas import AuthorCreate, AuthorUpdate

from .repositories import AuthorRepository
from .services import AuthorService


def author_repository_provider(session: AsyncSessionDep) -> AuthorRepository:
    return AuthorRepository(session)


AuthorRepositoryDep = Annotated[AuthorRepository, Depends(author_repository_provider)]


def author_service_dependency(author_repo: AuthorRepositoryDep) -> AuthorService:
    return AuthorService(author_repo)


BookServiceDep = Annotated[AuthorService, Depends(author_service_dependency)]


async def create_author_dependency(
    author_create: AuthorCreate,
    book_service: BookServiceDep,
) -> Author:
    return await book_service.create_author(author_create)


AuthorCreateDep = Annotated[Author, Depends(create_author_dependency)]


async def get_authors_list_dependency(book_service: BookServiceDep) -> list[Author]:
    return await book_service.get_authors_list()


AuthorsListDep = Annotated[list[Author], Depends(get_authors_list_dependency)]


async def get_author_by_id_dependency(
    author_id: UUID,
    book_service: BookServiceDep,
) -> Author:
    return await book_service.get_author_by_id(author_id)


AuthorIDDep = Annotated[Author, Depends(get_author_by_id_dependency)]


async def update_author_dependency(
    author_id: UUID,
    author_update: AuthorUpdate,
    book_service: BookServiceDep,
) -> Author:
    return await book_service.update_author(author_id, author_update)


AuthorUpdateDep = Annotated[Author, Depends(update_author_dependency)]
