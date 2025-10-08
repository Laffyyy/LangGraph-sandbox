import llms.deepseekLlms as deepseekllm
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


class UserPromptAgent:
	def __init__(self, llm=None):
		# If no llm is provided, use the shared deepseek_llm from the module
		self._invoke = deepseekllm.invoke if llm is None else (lambda prompt: llm.invoke(prompt))

	def refined_prompt(self, prompt: str) -> str:
		"""Refine the user prompt to be more specific and clear."""
		instructions = (
			"You are an expert prompt engineer. "
			"Refine the following user prompt to be more specific and clear:\n"

			"Don't change the meaning of the prompt, just make it clearer and more specific.\n"
			"Don't suggest any additional context or information.\n"
			"Return only the refined prompt, without any additional text.\n\n"
			
			f"User Prompt: {prompt}\n"
			"Refined Prompt:"
		)
		response = self._invoke(instructions)
		return response
    