import os
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    os.environ["POSTGRES_USER"],
    os.environ["POSTGRES_PASSWORD"],
    os.environ["POSTGRES_HOST"],
    os.environ["POSTGRES_PORT"],
    os.environ["POSTGRES_DATABASE"],
)

metadata = MetaData()
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
