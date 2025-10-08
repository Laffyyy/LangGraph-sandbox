import llms.deepseekLlms as deepseekllm
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class RouterAgent:
    def __init__(self, llm=None):
        # If no llm is provided, use the shared deepseek_llm from the module
        self._invoke = deepseekllm.invoke if llm is None else (lambda prompt: llm.invoke(prompt))

    def determine_task(self, prompt: str) -> str:
        """Determine the appropriate task for the given prompt."""
        instructions = (
            "You are an expert task router. "
            "Analyze the following user prompt and determine the most appropriate task to handle it.\n"
            "The available tasks are: Emailer, Scheduler, Chatbot.\n"
            "Return only the name of the task that best fits the prompt. If none fit, return 'None'.\n\n"
            
            f"User Prompt: {prompt}\n"
            "Task:"
        )
        response = self._invoke(instructions)
        return response.strip()