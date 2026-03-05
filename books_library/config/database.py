from typing import Annotated

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

from .path import ENVS_DIR


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 20
    max_overflow: int = 5
    echo: bool = False


class DatabaseConfig(BaseSettings):
    password: Annotated[str, Field(alias="POSTGRES_PASSWORD")] = "pass"
    user: Annotated[str, Field(alias="POSTGRES_USER")] = "user"
    host: Annotated[str, Field(alias="POSTGRES_HOST")] = "localhost"
    port: int = 5432
    name: Annotated[str, Field(alias="POSTGRES_DB")] = "library"
    sqla: SQLAlchemyConfig = SQLAlchemyConfig()

    model_config = SettingsConfigDict(
        env_file=ENVS_DIR / ".env.postgres-prod",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def url_sqla_pg_async(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
        )
