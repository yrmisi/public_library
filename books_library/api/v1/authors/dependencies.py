from typing import Annotated
from uuid import UUID

from fastapi import Depends

from database.models import Author
from dependencies.session import AsyncSessionDep
from exceptions import AuthorNotFoundError
from schemas import AuthorCreate

from .repositories import AuthorRepository


def repository_provider(session: AsyncSessionDep) -> AuthorRepository:
    return AuthorRepository(session)


AuthorRepositoryDep = Annotated[AuthorRepository, Depends(repository_provider)]


async def create_author(author_create: AuthorCreate, author_repo: AuthorRepositoryDep) -> Author:
    return await author_repo.create(author_create=author_create)


AuthorCreateDep = Annotated[Author, Depends(create_author)]


async def get_authors_list(author_repo: AuthorRepositoryDep) -> list[Author]:
    return await author_repo.list()


AuthorsListDep = Annotated[list[Author], Depends(get_authors_list)]


async def get_author_by_id(author_id: UUID, author_repo: AuthorRepositoryDep) -> Author:
    author = await author_repo.get_by_id(author_id=author_id)

    if author is not None:
        return author
    raise AuthorNotFoundError(author_id=author_id)


AuthorIDDep = Annotated[Author, Depends(get_author_by_id)]
