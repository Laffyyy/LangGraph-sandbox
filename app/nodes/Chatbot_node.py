import app.nodes.base_node as BaseNode

class ChatbotNode(BaseNode):
    def run(self, state):
        # Implement chatbot logic here
        state["chatbot_response"] = "This is a response from the chatbot."
        return state