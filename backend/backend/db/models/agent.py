from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from backend.db import db, metadata, sqlalchemy

agents = sqlalchemy.Table(
    "agents",
    metadata,
    sqlalchemy.Column(
        "id",
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
    ),
    sqlalchemy.Column("fullname", sqlalchemy.String, nullable=False),
)


class Agent:
    @classmethod
    async def get(cls, id):
        query = agents.select().where(agents.c.id == id)
        agent = await db.fetch_one(query)
        return agent

    @classmethod
    async def create(cls, **user):
        query = agents.insert().values(**user)
        agent_id = await db.execute(query)
        return agent_id

    @classmethod
    async def get_all(cls):
        query = agents.select()
        result = await db.fetch_all(query=query)
        return result


class AgentSchema(BaseModel):
    fullname: str

    class Config:
        orm_mode = True