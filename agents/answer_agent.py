# # # agents/answer_agent.py

# # import os
# # import requests
# # from dotenv import load_dotenv
# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain
# # from langchain_core.language_models.llms import LLM
# # from prompt_templates import answer_prompt
# # from typing import Optional, List

# # # Load environment variables from .env file
# # load_dotenv()

# # class TogetherLLM(LLM):
# #     model: str = "meta-llama/Llama-2-70b-chat-hf"
# #     api_url: str = "https://api.together.ai/v1/chat/completions"
# #     api_key: str = os.getenv("TOGETHER_API_KEY")

# #     def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
# #         """
# #         Makes a call to the Together.ai API with the provided prompt.
        
# #         :param prompt: The user input for which the model will generate a response.
# #         :param stop: Optional list of stop sequences to end the model's response.
# #         :return: The generated model response as a string.
# #         """
# #         headers = {
# #             "Authorization": f"Bearer {self.api_key}",
# #             "Content-Type": "application/json"
# #         }

# #         payload = {
# #             "model": self.model,
# #             "messages": [{"role": "user", "content": prompt}],
# #             "temperature": 0.7,
# #             "max_tokens": 512,
# #             "top_p": 0.9,
# #         }

# #         if stop:
# #             payload["stop"] = stop

# #         try:
# #             response = requests.post(self.api_url, json=payload, headers=headers)
# #             response.raise_for_status()  # Raise error for bad status codes
# #             result = response.json()

# #             # Extract and return the model's response
# #             return result["choices"][0]["message"]["content"]

# #         except requests.exceptions.RequestException as e:
# #             # Handle errors in the API call
# #             print(f"Error calling Together.ai API: {e}")
# #             return "An error occurred while fetching the response. Please try again later."

# #     @property
# #     def _llm_type(self) -> str:
# #         """
# #         Returns the type of language model being used.
# #         """
# #         return "together_llm"


# # def get_answer_agent() -> LLMChain:
# #     """
# #     Initializes and returns the answer agent chain with TogetherLLM.
# #     """
# #     llm = TogetherLLM()
# #     chain = LLMChain(llm=llm, prompt=answer_prompt)
# #     return chain




# # agents/answer_agent.py

# import os
# import requests
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_core.language_models.llms import LLM
# from prompt_templates import answer_prompt
# from typing import Optional, List

# # Load environment variables from .env file
# load_dotenv()

# class TogetherLLM(LLM):
#     model: str = "meta-llama/Llama-2-70b-chat-hf"
#     api_url: str = "https://api.together.ai/v1/chat/completions"
#     api_key: str = os.getenv("TOGETHER_API_KEY")

#     def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
#         """
#         Makes a call to the Together.ai API with the provided prompt.
#         """
#         headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json"
#         }

#         payload = {
#             "model": self.model,
#             "messages": [
#                 {"role": "system", "content": "You are a helpful and expert research assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             "temperature": 0.7,
#             "max_tokens": 512,
#             "top_p": 0.9
#         }

#         if stop:
#             payload["stop"] = stop

#         try:
#             response = requests.post(self.api_url, json=payload, headers=headers)
#             response.raise_for_status()
#             result = response.json()

#             return result["choices"][0]["message"]["content"].strip()

#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error: {http_err}")
#             print(f"Response content: {response.text}")
#         except Exception as err:
#             print(f"Unexpected error: {err}")

#         return "An error occurred while fetching the response. Please try again later."

#     @property
#     def _llm_type(self) -> str:
#         return "together_llm"


# def get_answer_agent() -> LLMChain:
#     """
#     Initializes and returns the answer agent chain with TogetherLLM.
#     """
#     llm = TogetherLLM()
#     chain = LLMChain(llm=llm, prompt=answer_prompt)
#     return chain







# agents/answer_agent.py

import os
import requests
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.language_models.llms import LLM
from prompt_templates import answer_prompt
from typing import Optional, List

load_dotenv()

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # ✅ updated to serverless-supported model
    api_url: str = "https://api.together.ai/v1/chat/completions"
    api_key: str = os.getenv("TOGETHER_API_KEY")

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful and expert research assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 512,
            "top_p": 0.9
        }

        if stop:
            payload["stop"] = stop

        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error: {http_err}")
            print(f"Response content: {response.text}")
        except Exception as err:
            print(f"Unexpected error: {err}")

        return "An error occurred while fetching the response. Please try again later."

    @property
    def _llm_type(self) -> str:
        return "together_llm"


def get_answer_agent() -> LLMChain:
    llm = TogetherLLM()
    chain = LLMChain(llm=llm, prompt=answer_prompt)
    return chain
