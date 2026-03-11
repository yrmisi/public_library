from fastapi import FastAPI

from api import router
from app_lifespan import lifespan
from config import settings
from exceptions import library_exception_handler, libraryBaseError

app = FastAPI(lifespan=lifespan, title=settings.app.title)

app.add_exception_handler(libraryBaseError, library_exception_handler)

app.include_router(router)
