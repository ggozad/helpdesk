import pdb
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.app import app
from backend.db import engine
from backend.db.models.agent import Agent, AgentSchema


@app.post("/agent/")
async def create_agent(agent: AgentSchema):
    async with AsyncSession(engine) as session:
        async with session.begin():
            obj = Agent(**agent.dict())
            session.add(obj)
        await session.refresh(obj)
    return {"agent_id": obj.id}


@app.get("/agents")
async def get_agents():
    async with AsyncSession(engine) as session:
        query = select(Agent)
        result = await session.execute(query)
    agents = [{"id": a.id, "fullname": a.fullname} for a in result.scalars()]
    return agents
