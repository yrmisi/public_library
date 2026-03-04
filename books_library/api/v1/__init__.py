from fastapi import APIRouter

from .books import router as books_router
from .health import router as health_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(books_router)
router.include_router(health_router)
