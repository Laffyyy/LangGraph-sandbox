import llms.deepseekLlms as deepseekllm

def __init_(self, llm: deepseekllm.DeepseekLlm):
    self.llm = llm

def refined_prompt(self, prompt: str) -> str:
    """Generate a refined prompt using the LLM."""
    instructions = (
        "You are an expert prompt engineer. "
        "Refine the following user prompt to be more specific and clear:\n"
        f"User Prompt: {prompt}\n"
        "Refined Prompt:"
    )
    response = self.llm.generate(instructions)

    return response
    