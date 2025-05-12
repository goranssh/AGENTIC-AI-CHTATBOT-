from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def greet(name):
    return f"Hello {name}, I'm your AI tutor. How can I help you today?"

tools = [
    Tool(
        name="Greeter",
        func=greet,
        description="Greets the student using their name"
    )
]

llm = ChatOpenAI(temperature=0, model="gpt-4")
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools, llm,
    agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Example conversation
print(agent.run("My name is Goransh."))
print(agent.run("Can you remind me what I told you before?"))
