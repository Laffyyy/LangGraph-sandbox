from pydantic import BaseModel, Field
from langsmith import traceable



@traceable
class AgentResponse(BaseModel):
    agent_response: str = Field(description="The agent's response")
    better_response: str = Field(description="The better response")
