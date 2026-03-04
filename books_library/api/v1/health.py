from fastapi import APIRouter

router = APIRouter(
    tags=["system"],
    include_in_schema=False,
)


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Website health check."""
    return {"status": "ok"}
