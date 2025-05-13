from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

# Set your API key
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the LLM
chat = ChatOpenAI(model="gpt-3.5-turbo")

# Start the loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    try:
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=user_input)
        ]
        response = chat.invoke(messages)
        print("Bot:", response.content)
    except Exception as e:
        print("Error:", e)
