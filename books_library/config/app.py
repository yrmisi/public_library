from pydantic import BaseModel


class AppConfig(BaseModel):
    """Configuration for the application."""

    title: str = "Books Library"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
