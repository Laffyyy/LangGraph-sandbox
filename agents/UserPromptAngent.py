from langgraph.prebuilt import create_react_agent

import os
import getpass

from langchain_anthropic import ChatAnthropic

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("DEEPSEEK_API_KEY")

deepseek_llm = ChatAnthropic(model="deepseek-chat")