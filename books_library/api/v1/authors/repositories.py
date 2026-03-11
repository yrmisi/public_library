from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Author
from schemas import AuthorCreate


class AuthorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self) -> list[Author]:
        stmt = select(Author).order_by(Author.id)
        authors = await self.session.scalars(stmt)

        return list(authors.all())

    async def get_by_id(self, author_id: UUID) -> Author | None:
        return await self.session.get(Author, author_id)

    async def create(self, author_create: AuthorCreate) -> Author:
        author = Author(**author_create.model_dump())

        self.session.add(author)
        await self.session.commit()

        return author
