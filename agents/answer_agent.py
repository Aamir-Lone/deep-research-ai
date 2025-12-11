

# import os
# import requests
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_core.language_models.llms import LLM
# from prompt_templates import answer_prompt
# from typing import Optional, List

# load_dotenv()

# class TogetherLLM(LLM):
#     model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"  
#     api_url: str = "https://api.together.ai/v1/chat/completions"
#     api_key: str = os.getenv("TOGETHER_API_KEY")

#     def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
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
#     llm = TogetherLLM()
#     chain = LLMChain(llm=llm, prompt=answer_prompt)
#     return chain




import os
import requests
from dotenv import load_dotenv

# Updated imports for modern LangChain layout
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_core.language_models.llms import LLM

from prompt_templates import answer_prompt
from typing import Optional, List

load_dotenv()

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
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
