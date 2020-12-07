from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL


Base = declarative_base()


class Agent(Base):
    __tablename__ = "agents"

    id = Column(
        "id",
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
    )
    fullname = Column("fullname", String, nullable=False)


class AgentSchema(BaseModel):
    fullname: str

    class Config:
        orm_mode = True