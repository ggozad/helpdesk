import os
from databases import Database
import sqlalchemy

DATABASE_URL = "postgres://{}:{}@{}:{}/{}".format(
    os.environ["POSTGRES_USER"],
    os.environ["POSTGRES_PASSWORD"],
    os.environ["POSTGRES_HOST"],
    os.environ["POSTGRES_PORT"],
    os.environ["POSTGRES_DATABASE"],
)

db = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
