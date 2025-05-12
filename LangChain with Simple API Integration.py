import openai
import requests
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentExecutor

# Define an API tool to fetch weather data (Replace with an actual API)
def fetch_weather(query):
    # Simulating an API call to get weather information
    # Replace with a real API call, such as to OpenWeatherMap or similar.
    return "The weather is sunny today!"

# Initialize the agent with a weather-fetching tool
tools = [
    Tool(
        name="WeatherFetcher",
        func=fetch_weather,
        description="Fetches weather information."
    ),
]

# Set up LangChain with OpenAI (GPT model)
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Initialize the agent with the tools
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Create an AgentExecutor to invoke the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Test the agent with a weather-related query
response = agent_executor.invoke({"input": "What is the weather like today?"})
print(response)
