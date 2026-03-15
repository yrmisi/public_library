from pydantic import BaseModel

from .app import AppConfig
from .database import DatabaseConfig


class Settings(BaseModel):
    """Configuration for the application."""

    db: DatabaseConfig = DatabaseConfig()
    app: AppConfig = AppConfig()


settings = Settings()
