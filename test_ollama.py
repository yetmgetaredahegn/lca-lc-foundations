from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
)

response = model.invoke(
    "Explain in one sentence what an AI agent is."
)

print(response.content)