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
    """Create a new author using the provided data."""
    return author_create


@router.get(
    "/",
    response_model=list[AuthorRead],
    status_code=status.HTTP_200_OK,
)
async def get_author_list(authors: AuthorsListDep) -> list[Author]:
    """Return a list of all authors."""
    return authors


@router.get(
    "/{author_id}",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
)
async def get_author_by_id(author: AuthorIDDep) -> Author:
    """Return an author by its ID."""
    return author


@router.patch(
    "/{author_id}",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
)
async def update_author(author: AuthorUpdateDep) -> Author:
    """Update an existing author and return the updated instance."""
    return author
