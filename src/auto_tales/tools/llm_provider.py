import os
from dotenv import load_dotenv
from crewai import LLM  # This is CrewAI's own LLM wrapper

load_dotenv()
def get_llm():
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        return LLM(
            model="groq/llama3-70b-8192",
            temperature=0.7,
            api_key=os.getenv("GROQ_API_KEY")
        )
    elif provider == "openai":
        return LLM(
            model="openai/gpt-4o",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    elif provider == "deepseek":
        return LLM(
            model="deepseek/deepseek-chat",
            temperature=0.7,
            api_key=os.getenv("DEEPSEEK_API_KEY"),
        )
    elif provider == "togetherai":
        return LLM(
            model="together_ai/meta-llama/Llama-Vision-Free",
            temperature=0.7,
            api_key=os.getenv("TOGETHERAI_API_KEY")
            # No base_url unless TogetherAI requires it
        )
    elif provider == "gemini":
        return LLM(
            model="gemini/gemini-2.0-flash",
            temperature=0.7,
            api_key=os.getenv("GEMINI_API_KEY"),
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
