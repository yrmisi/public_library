from fastapi import APIRouter

from .authors import router as authors_router
from .books import router as books_router
from .health import router as health_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(health_router)
router.include_router(books_router)
router.include_router(authors_router)
