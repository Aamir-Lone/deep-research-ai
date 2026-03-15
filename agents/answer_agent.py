

import os
from dotenv import load_dotenv
from langchain_together import ChatTogether
from langchain_core.output_parsers import StrOutputParser
from prompt_templates import answer_prompt

load_dotenv()

def get_answer_agent():
    llm = ChatTogether(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,
        max_tokens=512,
        top_p=0.9,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )
    chain = answer_prompt | llm | StrOutputParser()
    return chain

