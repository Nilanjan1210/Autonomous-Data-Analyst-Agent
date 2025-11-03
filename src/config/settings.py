import os
from dotenv import load_dotenv

def set_llm_api_key(api_key_name: str = "GROQ_API_KEY", show = False) -> str:
    load_dotenv()
    """Initialize the Groq LLM with API key."""
    api_key = os.getenv(api_key_name)

    if not api_key:
        api_key = input("Enter your GROQ API key: ").strip()
        os.environ[api_key_name] = api_key  

    if show == True:
        print(f"✅ {api_key_name} is set successfully.")
    return api_key



