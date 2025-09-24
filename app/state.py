import string
from pydantic import Field
from typing_extensions import Literal
from typing import List, Optional, TypedDict
from anthropic import BaseModel

class State(TypedDict, total=False):
	Task : str
	Nodepath: List[str]
	current_user: str
	user_input: str
	refined_prompt: str
	conversation_history: List[str]
	error_message: Optional[str]
	datestamp: str

class Routes(BaseModel):
	Routes: Literal["emailer", "scheduler", "chatbot", "default"] = Field(
		None , description="The route to take based on the user's task."
	)

# Backwards-compatibility alias
ConversationState = State


