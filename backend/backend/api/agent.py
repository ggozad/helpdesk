from backend.app import app
from backend.db.models.agent import Agent, AgentSchema
from typing import List, Optional


@app.post("/agent/")
async def create_agent(agent: AgentSchema):
    agent_id = await Agent.create(**agent.dict())
    return {"agent_id": agent_id}


@app.get("/agents")
async def get_agents():
    agents = await Agent.get_all()
    return agents