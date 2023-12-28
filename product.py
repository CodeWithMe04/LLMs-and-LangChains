from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

"""
This is make by Arin Chaudhary.
This code will tell you that we can also make AI with LangChain that provides LLMs.

"""

# Set up your OpenAI API key
qproduct = PromptTemplate.from_template("What is the name of ecommerce store that sells {product}")
llm = OpenAI(temperature=0.3, openai_api_key = "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")

finding = LLMChain(llm=llm, prompt=qproduct)
name = "MacBook"
answer = finding.run(name)
print(answer)