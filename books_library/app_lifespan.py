from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from database import async_engine


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, Any]:

    yield
    await async_engine.dispose()
