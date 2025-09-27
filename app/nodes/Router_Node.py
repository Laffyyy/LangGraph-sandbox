from app.State import State  

class RouterNode:
    def route(self, state:State) -> str:
        task = state.get("Task", "").lower()
        if task == "emailer":
            return "Emailer_Node"
        elif task == "scheduler":
            return "Scheduler_Node"
        elif task == "chatbot":
            return "Chatbot_Node"
        else:
            return "Default_Node"

    def run(self, state:State) -> str:
        return self.route(state)