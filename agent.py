from langchain.agents import create_agent

from llm import llm_gemini
from tools import kyphosis_predict
from langgraph.checkpoint.memory import InMemorySaver


tel_agent = create_agent(
    model=llm_gemini,
    tools=[kyphosis_predict],
    # checkpointer=InMemorySaver(),
    system_prompt="""
You are a helpful assistant that answers questions related to Kyphosis treatment. Use tool kyphosis_predict
which returns the absence or presence of kyphosis in the patient""")