from langgraph.prebuilt import create_react_agent

import os
import getpass

from langchain_openai import ChatOpenAI

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("DEEPSEEK_API_KEY")

deepseek_llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"  # DeepSeek's API endpoint
)

def invoke(prompt: str) -> str:
    """Invoke the DeepSeek LLM with a given prompt."""
    response = deepseek_llm.invoke(prompt)
    return response.content