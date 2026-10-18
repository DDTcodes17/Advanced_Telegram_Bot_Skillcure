from agent import tel_agent

user_prompt = "Search inside document, in which College dhruv studied?"

response = tel_agent.invoke({"messages":{"role":"user", "content": user_prompt}})
print(response['messages'][-1].content[0]['text'])