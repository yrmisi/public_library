from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .base import libraryBaseError


async def library_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, libraryBaseError):
        headers: dict[str, str] | None = getattr(exc, "headers", None)
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
            headers=headers,
        )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )
