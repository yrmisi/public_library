from collections.abc import AsyncIterable
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import async_session


async def session_dependency() -> AsyncIterable[AsyncSession]:
    """Provide an async SQLAlchemy session for a single request."""
    async with async_session() as session:
        yield session


AsyncSessionDep = Annotated[AsyncSession, Depends(session_dependency)]
