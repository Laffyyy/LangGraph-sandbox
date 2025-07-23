import llms.deepseekLlms as deepseekllm
import model.UserPromptModel as UserPromptModel


def UserPromptAgent(state: UserPromptModel):
    """This agent is used to generate a better prompt for the user."""
    reply = deepseekllm.invoke(f"Generate a better prompt for the user: {state.user_prompt}")
    return UserPromptModel(user_prompt=reply, better_prompt=reply)

