import app.nodes.base_node as BaseNode
import app.agents.EmailMakerAgent as EmailMakerAgent

class EmailerNode(BaseNode):
    def run(self, state):
        # Implement email sending logic here
        email_agent = EmailMakerAgent()
        
    