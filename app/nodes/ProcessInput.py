from app.nodes.base_node import BaseNode
from app.state import ConversationState

class ProcessInputNode(BaseNode):
    def run(self, state: ConversationState) -> ConversationState:
        state["user_input"] = state["user_input"].strip().lower()
        return state

# If you use State anywhere, change to state