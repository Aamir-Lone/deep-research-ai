

# # # # from langchain.agents import initialize_agent, AgentType
# # # # from langchain_community.tools.tavily_search import TavilySearchResults
# # # # from langchain_community.chat_models import ChatOpenAI
# # # # from dotenv import load_dotenv
# # # # import os

# # # # # Load environment variables from .env file
# # # # load_dotenv()

# # # # def get_research_agent():
# # # #     llm = ChatOpenAI(
# # # #         temperature=0,
# # # #         model="gpt-4",  # or gpt-3.5-turbo
# # # #         openai_api_key=os.getenv("OPENAI_API_KEY")  # securely loaded
# # # #     )

# # # #     tavily_tool = TavilySearchResults(k=5)
# # # #     tools = [tavily_tool]

# # # #     agent = initialize_agent(
# # # #         tools=tools,
# # # #         llm=llm,
# # # #         agent=AgentType.OPENAI_FUNCTIONS,
# # # #         verbose=True
# # # #     )

# # # #     return agent





# # # from langchain.agents import initialize_agent, AgentType
# # # from langchain_community.tools.tavily_search import TavilySearchResults
# # # from langchain_community.chat_models import ChatTogether
# # # from dotenv import load_dotenv
# # # import os

# # # # Load environment variables from .env file
# # # load_dotenv()

# # # def get_research_agent():
# # #     llm = ChatTogether(
# # #         together_api_key=os.getenv("TOGETHER_API_KEY"),  # Your Together API key
# # #         model="meta-llama/Llama-2-70b-chat-hf",  # Replace with your chosen model
# # #         temperature=0
# # #     )

# # #     tavily_tool = TavilySearchResults(k=5)
# # #     tools = [tavily_tool]

# # #     agent = initialize_agent(
# # #         tools=tools,
# # #         llm=llm,
# # #         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Assuming you want a zero-shot agent
# # #         verbose=True
# # #     )

# # #     return agent






# # from langchain.agents import initialize_agent, AgentType
# # from langchain_community.tools.tavily_search import TavilySearchResults
# # from dotenv import load_dotenv
# # import os
# # import requests

# # # Load environment variables from .env file
# # load_dotenv()

# # def get_research_agent():
# #     # Set the Together API endpoint and model
# #     together_api_url = "https://api.together.ai/v1/chat/completions"
# #     model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model

# #     # Headers for the API request
# #     headers = {
# #         "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
# #         "Content-Type": "application/json"
# #     }

# #     # Define a function to interact with Together API
# #     def call_together_api(prompt: str):
# #         payload = {
# #             "model": model,
# #             "messages": [{"role": "user", "content": prompt}],
# #         }
# #         response = requests.post(together_api_url, json=payload, headers=headers)
# #         response.raise_for_status()
# #         return response.json()

# #     # Define the Tavily search tool
# #     tavily_tool = TavilySearchResults(k=5)
# #     tools = [tavily_tool]

# #     # Initialize agent with tools and API interaction
# #     agent = initialize_agent(
# #         tools=tools,
# #         llm=call_together_api,  # Direct API call function
# #         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Assuming a zero-shot agent
# #         verbose=True
# #     )

# #     return agent




# from langchain.agents import initialize_agent, AgentType
# from langchain_community.tools.tavily_search import TavilySearchResults
# from dotenv import load_dotenv
# import os
# import requests
# from langchain_core.runnables import RunnableLambda

# # Load environment variables from .env file
# load_dotenv()

# def get_research_agent():
#     # Set the Together API endpoint and model
#     together_api_url = "https://api.together.ai/v1/chat/completions"
#     model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model

#     # Headers for the API request
#     headers = {
#         "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
#         "Content-Type": "application/json"
#     }

#     # Define a function to interact with Together API
#     def call_together_api(prompt: str):
#         payload = {
#             "model": model,
#             "messages": [{"role": "user", "content": prompt}],
#         }
#         response = requests.post(together_api_url, json=payload, headers=headers)
#         response.raise_for_status()
#         return response.json()

#     # Wrap the function as a Runnable
#     llm = RunnableLambda(func=call_together_api)

#     # Define the Tavily search tool
#     tavily_tool = TavilySearchResults(k=5)
#     tools = [tavily_tool]

#     # Initialize agent with tools and API interaction
#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,  # Pass the wrapped callable as llm
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Assuming a zero-shot agent
#         verbose=True
#     )

#     return agent






from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os
import requests
from langchain_core.runnables import RunnableLambda

# Load environment variables from .env file
load_dotenv()

def get_research_agent():
    # Set the Together API endpoint and model
    together_api_url = "https://api.together.ai/v1/chat/completions"
    model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model

    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
        "Content-Type": "application/json"
    }

    # Define a function to interact with Together API
    def call_together_api(inputs: dict, **kwargs):  # Changed to accept input dict and kwargs
        # prompt = inputs.get('prompt')
        prompt = str(inputs)
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }
        import json

        print("Headers:")
        print(json.dumps(headers, indent=2))
        print("Payload:")
        print(json.dumps(payload, indent=2))
        response = requests.post(together_api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    # Wrap the function as a Runnable
    llm = RunnableLambda(func=call_together_api)

    # Define the Tavily search tool
    tavily_tool = TavilySearchResults(k=5)
    tools = [tavily_tool]

    # Initialize agent with tools and API interaction
    agent = initialize_agent(
        tools=tools,
        llm=llm,  # Pass the wrapped callable as llm
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Assuming a zero-shot agent
        verbose=True
    )

    return agent
