from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

"""
This is make by Arin Chaudhary.
This code will tell you that we can also make AI with LangChain that provides LLMs.

"""

# Set up your OpenAI API key
qproduct = PromptTemplate.from_template("What is the name of ecommerce store that sells {product}")
llm = OpenAI(temperature=0.3, openai_api_key = "YOUR_OPENAI_API")

finding = LLMChain(llm=llm, prompt=qproduct, verbose=True)
name = "MacBook"
answer = finding.run(name)
print(answer)