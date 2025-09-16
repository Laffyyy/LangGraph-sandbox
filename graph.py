from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from model.UserPromptModel import UserPrompt
from agents.UserPromptAngent import UserPromptAgent
import llms.deepseekLlms as deepseekllm


def user_prompt_node(state: UserPrompt) -> UserPrompt:
    """Node that processes user prompts to generate better prompts."""
    return UserPromptAgent(state)


def create_graph():
    """Create and compile the LangGraph graph."""
    # Create the graph
    workflow = StateGraph(UserPrompt)
    
    # Add nodes
    workflow.add_node("user_prompt_agent", user_prompt_node)
    
    # Add edges
    workflow.add_edge(START, "user_prompt_agent")
    workflow.add_edge("user_prompt_agent", END)
    
    # Compile the graph
    app = workflow.compile()
    return app


# Create the compiled graph
graph = create_graph()