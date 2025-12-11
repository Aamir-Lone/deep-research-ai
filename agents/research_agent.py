

# from langchain.agents import initialize_agent, AgentType
# from langchain_community.tools.tavily_search import TavilySearchResults
# # from langchain_community.chat_models import ChatTogether
# from langchain_together import ChatTogether

# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_research_agent():
#     tavily_tool = TavilySearchResults(k=5)
#     tools = [tavily_tool]


#     llm = ChatTogether(
#         model="mistralai/Mixtral-8x7B-Instruct-v0.1",
#         temperature=0.7,
#         max_tokens=512,
#         top_p=0.95,
#         together_api_key=os.getenv("TOGETHER_API_KEY")
#     )

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True
#     )

#     return agent






from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_together import ChatTogether

from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()


def get_research_agent():
    # Tavily Search Tool
    tavily_tool = TavilySearchResults(k=5)
    tools = [tavily_tool]

    # LLM for reasoning + tool calling
    llm = ChatTogether(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,
        max_tokens=512,
        top_p=0.95,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )

    # Prompt for ReAct agent (required by new API)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research assistant. Use tools when needed and provide detailed findings."),
        ("human", "{input}")
    ])

    # Build a ReAct-style agent
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    # Wrap inside AgentExecutor (replacement for initialize_agent)
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    return executor
