from datetime import datetime, timedelta
import os
from typing import Mapping
from jose import jwt


SECRET = os.environ.get("AUTH_SECRET")


def tokenize(data: dict, expires: timedelta = None) -> str:
    if expires is not None and data.get("exp") is None:
        data["exp"] = datetime.utcnow() + expires
    return jwt.encode(
        data,
        SECRET,
        algorithm="HS256",
    )


def detokenize(token: str) -> Mapping:
    return jwt.decode(token, SECRET)
