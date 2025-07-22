from pydantic import BaseModel, Field
from langsmith import traceable

@traceable
class UserPrompt(BaseModel):
    user_prompt: str = Field(description="The user's prompt")
    better_prompt: str = Field(description="The better prompt")
