from uuid import UUID

from database import Book
from fastapi import APIRouter, status
from schemas import BookCreate, BookRead

from .dependencies import BooksListDp

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.post(
    "/",
    response_model=BookCreate,
    status_code=status.HTTP_201_CREATED,
)
def create_books(book: BookCreate) -> Book:
    pass


@router.get(
    "/",
    response_model=list[BookRead],
    status_code=status.HTTP_200_OK,
)
async def get_books(books: BooksListDp) -> list[Book]:
    return books


@router.get(
    "/{book_id}/",
    response_model=BookRead,
    status_code=status.HTTP_200_OK,
)
def get_book_by_id(book_id: UUID) -> Book:
    pass
