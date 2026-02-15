from fastapi import FastAPI

from api import router
from app_lifespan import lifespan
from config import settings

app = FastAPI(lifespan=lifespan, title=settings.app.title)

app.include_router(router)
