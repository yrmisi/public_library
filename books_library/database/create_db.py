from config import settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

async_engine = create_async_engine(
    url=settings.db.url_sqla_pg_async,
    echo=settings.db.sqla.echo,
    pool_size=settings.db.sqla.pool_size,
    max_overflow=settings.db.sqla.max_overflow,
)

async_session = async_sessionmaker(
    async_engine,
    autoflush=False,
    expire_on_commit=False,
    autocommit=False,
)
