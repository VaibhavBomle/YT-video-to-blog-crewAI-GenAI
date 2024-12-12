from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM
def get_LLM():
  openai_api_key = os.getenv("OPENAI_API_KEY")
  llm = ChatOpenAI(
    model="gpt-4-0125-preview",
    temperature=0,
    openai_api_key= openai_api_key
   )
  return llm