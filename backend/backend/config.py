import os
from functools import lru_cache
from pydantic import (
    BaseSettings,
    PostgresDsn,
    Field,
)

DOT_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../etc/.env")


class Settings(BaseSettings):

    pg_dsn: PostgresDsn = Field(..., env="db_dsn")

    class Config:
        env_file = DOT_ENV_PATH
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()
