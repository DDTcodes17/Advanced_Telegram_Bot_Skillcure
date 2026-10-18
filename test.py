from agent import tel_agent

user_prompt = "I have a patient 71 years old with 12 number vertebrae involved and 7 number of first vertebra operated on. Detect whether the patient has kyphosis or not."

response = tel_agent.invoke({"messages":{"role":"user", "content": user_prompt}})
print(response['messages'][0].content)