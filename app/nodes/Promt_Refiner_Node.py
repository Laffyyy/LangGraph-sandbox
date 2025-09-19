from app.state import ConversationState
from app.agents.UserPromptAngent import UserPromptAgent

class PromptRefinerNode:
    def __init__(self, agent: UserPromptAgent):
        self.agent = agent
    def run(self, state: ConversationState) -> ConversationState:
        refined = self.agent.refined_prompt(state.user_input[-1])
        state.refined_prompt = refined
        return state