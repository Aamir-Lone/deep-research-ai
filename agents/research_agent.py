

from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain_community.chat_models import ChatTogether
from langchain_together import ChatTogether

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

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
