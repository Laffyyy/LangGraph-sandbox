from app.State import State
from app.agents.UserPromptAngent import UserPromptAgent


class PromptRefinerNode:
	def __init__(self):
		self.agent = UserPromptAgent()

	def run(self, state: State) -> State:
		latest_input = state.get("user_input", "")
		if isinstance(latest_input, list):
			latest_input = latest_input[-1] if latest_input else ""
		refined = self.agent.refined_prompt(str(latest_input))
		state["refined_prompt"] = refined
		return state