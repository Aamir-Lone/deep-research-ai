

from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_together import ChatTogether
from langchain import hub
from dotenv import load_dotenv
import os

load_dotenv()

def get_research_agent():
    tavily_tool = TavilySearchResults(k=5)
    tools = [tavily_tool]

    llm = ChatTogether(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,
        max_tokens=512,
        top_p=0.95,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )

    # Use a standard prompt from LangChain Hub for ReAct agents
    prompt = hub.pull("hwchase17/react")

    # Construct the ReAct agent
    agent = create_react_agent(llm, tools, prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    return agent_executor
