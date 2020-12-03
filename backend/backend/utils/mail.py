from functools import lru_cache
from typing import List
import os

from fastapi_mail import FastMail, ConnectionConfig
from pydantic import EmailStr, BaseModel


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME=os.environ["MAIL_USERNAME"],
    MAIL_PASSWORD=os.environ["MAIL_PASSWORD"],
    MAIL_FROM=os.environ["MAIL_FROM"],
    MAIL_PORT=int(os.environ["MAIL_PORT"]),
    MAIL_SERVER=os.environ["MAIL_HOSTNAME"],
    MAIL_TLS=bool(os.environ["MAIL_TLS"]),
    MAIL_SSL=bool(os.environ["MAIL_SSL"]),
)

mailer = FastMail(conf)


@lru_cache()
def get_mailer():
    return mailer
