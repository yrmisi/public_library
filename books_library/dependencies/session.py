from collections.abc import AsyncIterable
from typing import Annotated

from database import async_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def session_dependency() -> AsyncIterable[AsyncSession]:
    async with async_session() as session:
        yield session


AsyncSessionDp = Annotated[AsyncSession, Depends(session_dependency)]
