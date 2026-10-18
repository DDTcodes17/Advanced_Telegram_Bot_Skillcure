import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

llm_gemini = ChatGoogleGenerativeAI(
    model = "gemini-3.1-flash-lite",
    temperature = 0.59
)