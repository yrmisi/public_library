from fastapi import APIRouter, status

from database.models import Book
from schemas import BookCreate, BookRead

from .dependencies import BookCreateDep, BookIDDep, BooksListDep, BookUpdateDep

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.post(
    "/",
    response_model=BookCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(book_create: BookCreateDep) -> Book:
    return book_create


@router.get(
    "/",
    response_model=list[BookRead],
    status_code=status.HTTP_200_OK,
)
async def get_books(books: BooksListDep) -> list[Book]:
    return books


@router.get(
    "/{book_id}",
    response_model=BookRead,
    status_code=status.HTTP_200_OK,
)
async def get_book_by_id(book: BookIDDep) -> Book:
    return book


@router.patch(
    "/{book_id}",
    response_model=BookRead,
    status_code=status.HTTP_200_OK,
)
async def update_book(book: BookUpdateDep) -> Book:
    return book
