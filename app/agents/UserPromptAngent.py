import llms.deepseekLlms as deepseekllm


class UserPromptAgent:
	def __init__(self, llm=None):
		# If no llm is provided, use the shared deepseek_llm from the module
		self._invoke = deepseekllm.invoke if llm is None else (lambda prompt: llm.invoke(prompt))

	def refined_prompt(self, prompt: str) -> str:
		instructions = (
			"You are an expert prompt engineer. "
			"Refine the following user prompt to be more specific and clear:\n"
			f"User Prompt: {prompt}\n"
			"Refined Prompt:"
		)
		response = self._invoke(instructions)
		return response
    