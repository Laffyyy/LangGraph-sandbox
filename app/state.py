import string
from typing import List, Optional, TypedDict


class State(TypedDict, total=False):
	Nodepath: List[str]
	current_user: str
	user_input: str
	refined_prompt: str
	conversation_history: List[str]
	error_message: Optional[str]
	datestamp: str

# Backwards-compatibility alias
ConversationState = State


