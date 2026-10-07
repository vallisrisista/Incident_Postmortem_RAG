import os
from langchain_google_genai import ChatGoogleGenerativeAI
import time

from langsmith import traceable


@traceable
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0,
    )

@traceable
def _text(resp) -> str:
    c = resp.content
    if isinstance(c, str):
        return c
    return "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in c)