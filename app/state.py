import string
from typing import List
from pydantic import BaseModel


class ConversationState(BaseModel):
    Nodepath: List[str]
    current_user: str
    user_input: List[str]
    refined_prompt: str
    conversation_history: List[str] 
    error_message: str
    datestamp: List[str]


