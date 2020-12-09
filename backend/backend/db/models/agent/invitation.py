from enum import unique
from pydantic.networks import EmailStr
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from backend.db import Base
from typing import Optional


class AgentInvitation(Base):
    __tablename__ = "agent_invitations"

    email = Column("email", String, primary_key=True)
    role = Column("role", String)
    token = Column("token", String, nullable=False)


class AgentInvitationSchema(BaseModel):
    email: EmailStr
    role: Optional[str]

    class Config:
        orm_mode = True