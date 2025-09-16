import llms.deepseekLlms as deepseekllm
from model.UserPromptModel import UserPrompt


def UserPromptAgent(state: UserPrompt):
    """This agent is used to generate a better prompt for the user."""
    reply = deepseekllm.invoke(f"Generate a better prompt for the user: {state.user_prompt}")
    return UserPrompt(user_prompt=reply, better_prompt=reply)

