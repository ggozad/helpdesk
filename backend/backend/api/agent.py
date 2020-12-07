from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from backend.app import app
from backend.db import engine
from backend.db.models.agent import Agent, AgentRole, AgentSchema


@app.post("/agent/")
async def create_agent(agent: AgentSchema):
    async with AsyncSession(engine) as session:
        async with session.begin():
            obj = Agent(
                fullname=agent.fullname, roles=[AgentRole(role=r) for r in agent.roles]
            )
            session.add(obj)
        await session.refresh(obj)
    return {"agent_id": obj.id}


@app.get("/agents")
async def get_agents():
    async with AsyncSession(engine) as session:
        query = select(Agent).options(selectinload(Agent.roles))
        result = await session.execute(query)
    agents = [
        {"id": a.id, "fullname": a.fullname, "roles": a.roles} for a in result.scalars()
    ]
    return agents
