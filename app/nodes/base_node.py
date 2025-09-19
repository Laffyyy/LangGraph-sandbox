from app.state import State

class BaseNode:
    def run(self, state: State) -> State:
        raise NotImplementedError("subclasses should implement this method (run()).")