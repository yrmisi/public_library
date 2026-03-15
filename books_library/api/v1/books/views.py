from fastapi import APIRouter, status

from database.models import Book
from schemas import BookRead

from .dependencies import BookCreateDep, BookIDDep, BooksListDep, BookUpdateDep

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.post(
    "/",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(book: BookCreateDep) -> Book:
    """Create a new book using the provided data."""
    return book


@router.get(
    "/",
    response_model=list[BookRead],
    status_code=status.HTTP_200_OK,
)
async def get_books(books: BooksListDep) -> list[Book]:
    """Return a list of all books."""
    return books


@router.get(
    "/{book_id}",
    response_model=BookRead,
    status_code=status.HTTP_200_OK,
)
async def get_book_by_id(book: BookIDDep) -> Book:
    """Return a book by its ID."""
    return book


@router.patch(
    "/{book_id}",
    response_model=BookRead,
    status_code=status.HTTP_200_OK,
)
async def update_book(book: BookUpdateDep) -> Book:
    """Update an existing book and return the updated instance."""
    return book
