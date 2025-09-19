from langgraph.graph import StateGraph, START, END
from app.State import State
from app.nodes.ProcessInput_Node import ProcessInputNode
from app.nodes.Promt_Refiner_Node import PromptRefinerNode


def build_graph():
	workflow = StateGraph(State)
	process_node = ProcessInputNode()
	refiner_node = PromptRefinerNode()
	workflow.add_node("process_input", process_node.run)
	workflow.add_node("user_prompt_agent", refiner_node.run)
	workflow.add_edge(START, "process_input")
	workflow.add_edge("process_input", "user_prompt_agent")
	workflow.add_edge("user_prompt_agent", END)
	return workflow.compile()