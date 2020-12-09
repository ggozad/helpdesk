from pydantic import BaseModel
from pydantic.networks import EmailStr
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional

from backend.db import Base
from .agent import AgentRoleEnum


class AgentInvitation(Base):
    __tablename__ = "agent_invitations"

    email = Column("email", String, primary_key=True)
    role = Column("role", String)
    token = Column("token", String, nullable=False)


class AgentInvitationSchema(BaseModel):
    email: EmailStr
    role: Optional[AgentRoleEnum]

    class Config:
        orm_mode = True