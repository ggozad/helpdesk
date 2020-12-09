from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from enum import Enum
from pydantic import BaseModel
from pydantic.networks import EmailStr
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from typing import List

from backend.db import Base

# Models
class Agent(Base):
    __tablename__ = "agents"

    id = Column(
        "id",
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
    )
    fullname = Column("fullname", String, nullable=False)
    email = Column("email", String, nullable=False)
    roles = relationship("AgentRole")


class AgentRole(Base):
    __tablename__ = "agent_roles"
    __table_args__ = (PrimaryKeyConstraint("agent_id", "role"),)
    agent_id = Column(ForeignKey("agents.id"))

    role = Column("role", String, nullable=False)


# Schemas
class AgentRoleEnum(str, Enum):
    admin = "admin"


class AgentSchema(BaseModel):
    fullname: str
    roles: List[AgentRoleEnum]
    email: EmailStr

    class Config:
        orm_mode = True