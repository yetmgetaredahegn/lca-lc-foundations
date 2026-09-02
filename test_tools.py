from langchain_ollama import ChatOllama
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


model = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
)

model_with_tools = model.bind_tools([multiply])

response = model_with_tools.invoke(
    "What is 125 multiplied by 48? Use the multiply tool."
)

print("Response:")
print(response)

print("\nTool calls:")
print(response.tool_calls)