import uvicorn

from config import settings


def main():
    uvicorn.run(
        "app:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
    )


if __name__ == "__main__":
    main()
