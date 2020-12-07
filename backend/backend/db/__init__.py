import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    os.environ["POSTGRES_USER"],
    os.environ["POSTGRES_PASSWORD"],
    os.environ["POSTGRES_HOST"],
    os.environ["POSTGRES_PORT"],
    os.environ["POSTGRES_DATABASE"],
)

Base = declarative_base()

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
