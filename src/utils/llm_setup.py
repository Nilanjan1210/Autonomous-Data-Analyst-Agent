from langchain_groq import ChatGroq
import os
import sys
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config.settings import set_llm_api_key

def get_llm(model: str = "openai/gpt-oss-120b", temperature: float = 1.0) -> ChatGroq:
    """
    Returns a ChatGroq LLM instance with the given model and temperature.
    """
    return ChatGroq(
        model=model,
        temperature=temperature
    )



