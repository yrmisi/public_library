from pydantic import BaseModel

from .app import AppConfig
from .database import DatabaseConfig


class Settings(BaseModel):
    db: DatabaseConfig = DatabaseConfig()
    app: AppConfig = AppConfig()


settings = Settings()
