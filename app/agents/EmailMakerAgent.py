import llms.deepseekLlms as deepseekllm
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class EmailMakerAgent:
    def __init__(self, llm=None):
        # If no llm is provided, use the shared deepseek_llm from the module
        self._invoke = deepseekllm.invoke if llm is None else (lambda prompt: llm.invoke(prompt))

    def create_email(self, prompt: str) -> str:
        """Generate an email based on the given prompt."""
        instructions = (
            "You are an expert email generator. "
            "Make sure the email is clear, concise, and professional.\n"
            "Based on the following user prompt, create a professional and well-structured email.\n\n"
            
            f"User Prompt: {prompt}\n"
            "Email:"
        )
        response = self._invoke(instructions)
        return response.strip()