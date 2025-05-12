
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentExecutor

# Define the tools that the agent can use
tools = [
    Tool(
        name="Calculator",
        func=lambda query: eval(query),
        description="A tool to perform simple calculations"
    ),
    Tool(
        name="WeatherFetcher",
        func=lambda query: "The weather is sunny.",  # Example: integrate with an actual weather API
        description="Fetches weather information."
    ),
]

# Initialize the agent
llm = ChatOpenAI(model="gpt-4", temperature=0)
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Execute the agent with a query
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke({"input": "What is 5+3?"})
print(response)
