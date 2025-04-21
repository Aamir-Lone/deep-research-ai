# # # # # agents/answer_agent.py

# # # # from langchain.prompts import PromptTemplate
# # # # # from langchain.chat_models import ChatOpenAI
# # # # from langchain_community.chat_models import ChatOpenAI

# # # # from langchain.chains import LLMChain
# # # # from prompt_templates import answer_prompt

# # # # def get_answer_agent():
# # # #     llm = ChatOpenAI(temperature=0.3, model="gpt-4")
# # # #     chain = LLMChain(llm=llm, prompt=answer_prompt)
# # # #     return chain




# # # # agents/answer_agent.py

# # # from langchain.prompts import PromptTemplate
# # # from langchain_community.chat_models import ChatTogether
# # # from langchain.chains import LLMChain
# # # from prompt_templates import answer_prompt
# # # from dotenv import load_dotenv
# # # import os

# # # # Load environment variables from .env file
# # # load_dotenv()

# # # def get_answer_agent():
# # #     llm = ChatTogether(
# # #         together_api_key=os.getenv("TOGETHER_API_KEY"),  # Your Together API key
# # #         model="meta-llama/Llama-2-70b-chat-hf",  # Replace with your chosen model
# # #         temperature=0.3
# # #     )
# # #     chain = LLMChain(llm=llm, prompt=answer_prompt)
# # #     return chain



# # # agents/answer_agent.py

# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain
# # from prompt_templates import answer_prompt
# # from dotenv import load_dotenv
# # import os
# # import requests

# # # Load environment variables from .env file
# # load_dotenv()

# # # Define a function to interact with Together API
# # def call_together_api(prompt: str):
# #     together_api_url = "https://api.together.ai/v1/chat/completions"
# #     model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model
# #     headers = {
# #         "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
# #         "Content-Type": "application/json"
# #     }
# #     payload = {
# #         "model": model,
# #         "messages": [{"role": "user", "content": prompt}],
# #     }
# #     response = requests.post(together_api_url, json=payload, headers=headers)
# #     response.raise_for_status()
# #     return response.json()

# # def get_answer_agent():
# #     chain = LLMChain(llm=call_together_api, prompt=answer_prompt)
# #     return chain






# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain
# # from prompt_templates import answer_prompt
# # from dotenv import load_dotenv
# # import os
# # import requests

# # # Load environment variables from .env file
# # load_dotenv()

# # # Define a function to interact with Together API
# # def call_together_api(inputs: dict, **kwargs):  # Changed to accept input dict and kwargs
# #     together_api_url = "https://api.together.ai/v1/chat/completions"
# #     model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model
# #     headers = {
# #         "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
# #         "Content-Type": "application/json"
# #     }

# #     if isinstance(inputs, dict):
# #         prompt = inputs.get('prompt')
# #     else:
# #         prompt = inputs.value

# #     # # prompt = inputs.get('prompt')  # Extract the prompt from inputs
# #     # prompt = inputs.value('prompt')
# #     payload = {
# #         "model": model,
# #         "messages": [{"role": "user", "content": prompt}],
# #     }
# #     response = requests.post(together_api_url, json=payload, headers=headers)
# #     response.raise_for_status()
# #     return response.json()

# # def get_answer_agent():
# #     chain = LLMChain(llm=call_together_api, prompt=answer_prompt)
# #     return chain






# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from prompt_templates import answer_prompt
# from dotenv import load_dotenv
# import os
# import requests
# from langchain.prompts import StringPromptValue  # Import StringPromptValue to check input type

# # Load environment variables from .env file
# load_dotenv()

# # Define a function to interact with Together API
# def call_together_api(inputs, **kwargs):  # No need for type hinting as inputs could vary
#     together_api_url = "https://api.together.ai/v1/chat/completions"
#     model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model
#     headers = {
#         "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
#         "Content-Type": "application/json"
#     }

#     # Check if inputs is a dictionary or a StringPromptValue object
#     if isinstance(inputs, dict):
#         prompt = inputs.get('prompt')  # Extract the prompt if it's a dictionary
#     elif isinstance(inputs, StringPromptValue):
#         prompt = str(inputs)  # Convert StringPromptValue to string if it's an instance of that class
#     else:
#         raise ValueError("Expected inputs to be a dictionary or StringPromptValue")

#     # Prepare the payload for the request
#     payload = {
#         "model": model,
#         "messages": [{"role": "user", "content": prompt}],
#     }
    
#     # Make the request to the Together API
#     response = requests.post(together_api_url, json=payload, headers=headers)
#     response.raise_for_status()  # Ensure we handle errors properly
#     return response.json()

# # Define a function to create and return the answer agent
# def get_answer_agent():
#     chain = LLMChain(llm=call_together_api, prompt=answer_prompt)
#     return chain




from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from prompt_templates import answer_prompt
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Define a function to interact with Together API
def call_together_api(inputs, **kwargs):  # No need for type hinting as inputs could vary
    together_api_url = "https://api.together.ai/v1/chat/completions"
    model = "meta-llama/Llama-2-70b-chat-hf"  # Choose your model
    headers = {
        "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
        "Content-Type": "application/json"
    }

    # Check if inputs is a dictionary or a simple string
    if isinstance(inputs, dict):
        prompt = inputs.get('prompt')  # Extract the prompt if it's a dictionary
    elif isinstance(inputs, str):
        prompt = inputs  # Use the string directly if inputs is a string
    else:
        raise ValueError("Expected inputs to be a dictionary or string")

    # Prepare the payload for the request
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    
    # Make the request to the Together API
    response = requests.post(together_api_url, json=payload, headers=headers)
    response.raise_for_status()  # Ensure we handle errors properly
    return response.json()

# Define a function to create and return the answer agent
def get_answer_agent():
    chain = LLMChain(llm=call_together_api, prompt=answer_prompt)
    return chain
