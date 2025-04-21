# # prompt_templates.py

# from langchain.prompts import PromptTemplate

# answer_prompt = PromptTemplate(
#     input_variables=["query", "context"],
#     template="""
# You are an expert research assistant.

# Based on the following web-gathered content, answer the question thoroughly.

# Question: {query}

# Context:
# {context}

# Give a structured and detailed answer, including any relevant citations or links if available.
# """
# )






# prompt_templates.py

from langchain.prompts import PromptTemplate

answer_prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="""
You are an expert research assistant.

Based on the following web-gathered content, answer the question thoroughly.

Question: {query}

Context:
{context}

Give a structured and detailed answer, including any relevant citations or links if available.
"""
)
