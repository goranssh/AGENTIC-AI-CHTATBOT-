from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

def read_file(_):
    with open("notes.txt", "r") as file:
        return file.read()

tools = [
    Tool(
        name="NoteReader",
        func=read_file,
        description="Reads content from a file called notes.txt"
    )
]

llm = ChatOpenAI(model="gpt-4", temperature=0)
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

print(agent.run("Read the notes and tell me what it's about."))
