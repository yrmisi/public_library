from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database.models import Author
from schemas import AuthorCreate


class AuthorRepository:
    """Data access layer for Author entities."""

    def __init__(self, session: AsyncSession):
        """Initialize the AuthorRepository with a database session."""
        self.session = session

    async def list(self) -> list[Author]:
        """Return all authors ordered by ID, eagerly loading related books."""
        stmt = select(Author).options(selectinload(Author.books)).order_by(Author.id)
        authors = await self.session.scalars(stmt)

        return list(authors.all())

    async def get_by_id(self, author_id: UUID) -> Author | None:
        """Return an author by ID or None if it does not exist."""
        return await self.session.get(Author, author_id)

    async def create(self, author_create: AuthorCreate) -> Author:
        """Create and persist a new author entity."""
        author = Author(**author_create.model_dump())

        self.session.add(author)
        await self.session.commit()

        return author

    async def update(
        self,
        author: Author,
        update_data: dict[str, str | bool],
    ) -> None:
        """Apply partial updates to an author and sync changes to the database."""
        for key, val in update_data.items():
            setattr(author, key, val)

        await self.session.commit()
        await self.session.refresh(author)
