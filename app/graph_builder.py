from langgraph.graph import StateGraph, START, END
from app.State import State
from app.nodes.ProcessInput_Node import ProcessInputNode
from app.nodes.Promt_Refiner_Node import PromptRefinerNode
from app.nodes.Router_Node import RouterNode
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file



def build_graph():
	workflow = StateGraph(State)
			
	process_node = ProcessInputNode()
	refiner_node = PromptRefinerNode()
	router_node = RouterNode()
	

	workflow.add_node("process_input", process_node.run)
	workflow.add_node("user_prompt_agent", refiner_node.run)
	workflow.add_node("router", router_node.run)



	workflow.add_edge(START, "process_input")
	workflow.add_edge("process_input", "user_prompt_agent")
	workflow.add_edge("user_prompt_agent", "router")
	workflow.add_conditional_edges("router", {
		"Emailer_Node": "emailer_node",
		"Scheduler_Node": "scheduler_node",
		"Chatbot_Node": "chatbot_node",
		"Default_Node": END
	})

	workflow.add_edge("router", END)
	return workflow.compile()