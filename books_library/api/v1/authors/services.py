from uuid import UUID

from database.models import Author
from exceptions import AuthorNotFoundError
from schemas import AuthorCreate, AuthorUpdate

from .repositories import AuthorRepository


class AuthorService:
    def __init__(self, author_repo: AuthorRepository) -> None:
        self.author_repo = author_repo

    async def create_author(self, author_create: AuthorCreate) -> Author:
        return await self.author_repo.create(author_create=author_create)

    async def get_authors_list(self) -> list[Author]:
        return await self.author_repo.list()

    async def get_author_by_id(self, author_id: UUID) -> Author:
        author: Author | None = await self.author_repo.get_by_id(author_id=author_id)

        if author is None:
            raise AuthorNotFoundError(author_id=author_id)

        return author

    async def update_author(
        self,
        author_id: UUID,
        author_update: AuthorUpdate,
    ) -> Author:
        async with self.author_repo.session.begin():
            author: Author | None = await self.author_repo.get_by_id(author_id=author_id)

            if author is None:
                raise AuthorNotFoundError(author_id=author_id)

            update_data: dict[str, str | bool] = author_update.model_dump(exclude_unset=True)

            await self.author_repo.update(author, update_data)

            return author
