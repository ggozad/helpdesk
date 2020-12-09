from backend.db.models.agent.invitation import AgentInvitation
from datetime import timedelta
from fastapi_mail import MessageSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from backend.app import app
from backend.db import engine
from backend.db.models.agent import Agent, AgentRole, AgentSchema, AgentInvitationSchema
from backend.crypto import tokenize
from backend.utils.mail import get_mailer


@app.post("/agent/")
async def create_agent(agent: AgentSchema):
    async with AsyncSession(engine) as session:
        async with session.begin():
            obj = Agent(
                fullname=agent.fullname,
                email=agent.email,
                roles=[AgentRole(role=r) for r in agent.roles],
            )
            session.add(obj)
        await session.refresh(obj)
    return {"agent_id": obj.id}


@app.get("/agents")
async def get_agents():
    async with AsyncSession(engine) as session:
        query = select(Agent).options(joinedload(Agent.roles))
        result = await session.execute(query)
        result = result.unique().scalars().all()

    agents = [
        {
            "id": a.id,
            "fullname": a.fullname,
            "email": a.email,
            "roles": [r.role for r in a.roles],
        }
        for a in result
    ]
    return agents


@app.post("/agent/invitation")
async def invite_agent(invitation: AgentInvitationSchema):
    """
    Creates an invitation token for a new agent and sends it to her email address.
    The invitation expires in 7 days.
    """

    token = tokenize(invitation.dict(), expires=timedelta(days=7))

    async with AsyncSession(engine) as session:
        async with session.begin():
            obj = AgentInvitation(
                email=invitation.email, role=invitation.role, token=token
            )
            await session.merge(obj)

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=[invitation.email],
        body="""
            <p>You have been invited. Token: {}</p>
        """.format(
            token
        ),
        subtype="html",
    )
    mailer = get_mailer()
    await mailer.send_message(message)
    return {}
