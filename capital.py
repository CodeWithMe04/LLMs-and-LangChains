from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

"""
This is make by Arin Chaudhary.
This code will tell you that we can also make AI with LangChain that provides LLMs.

"""

# cities = [
#     "Patna",
#     "Delhi",
#     "Chennai",
# ]

# Set up your OpenAI API key
qcity = PromptTemplate.from_template("What is the capital of {place}")
llm = OpenAI(temperature=0.3, openai_api_key = "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")
# print(llm.predict("What is capital of India?"))

chain = LLMChain(llm=llm, prompt=qcity)
city = "USA"
output = chain.run(city)
print(output)