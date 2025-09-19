from app.nodes.base_node import BaseNode
from app.State import State


class ProcessInputNode(BaseNode):
	def run(self, state: State) -> State:
		latest_input = state.get("user_input", "")
		if isinstance(latest_input, list):
			latest_input = latest_input[-1] if latest_input else ""
		if isinstance(latest_input, str):
			latest_input = latest_input.strip().lower()
		state["user_input"] = latest_input
		return state