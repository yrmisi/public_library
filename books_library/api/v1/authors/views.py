from fastapi import APIRouter, status

from database.models import Author
from schemas import AuthorRead

from .dependencies import AuthorCreateDep, AuthorIDDep, AuthorsListDep, AuthorUpdateDep

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)


@router.post(
    "/",
    response_model=AuthorRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_author(author_create: AuthorCreateDep) -> Author:
    return author_create


@router.get(
    "/",
    response_model=list[AuthorRead],
    status_code=status.HTTP_200_OK,
)
async def get_author_list(authors: AuthorsListDep) -> list[Author]:
    return authors


@router.get(
    "/{author_id}",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
)
async def get_author_by_id(author: AuthorIDDep) -> Author:
    return author


@router.patch(
    "/{author_id}",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
)
async def update_author(author: AuthorUpdateDep) -> Author:
    return author
