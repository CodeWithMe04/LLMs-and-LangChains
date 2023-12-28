from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

"""
This is make by Arin Chaudhary.
This code will tell you that we can also make AI with LangChain that provides LLMs.

"""

# Set up your OpenAI API key
qroler = PromptTemplate.from_template("Who is the PM/President of {country}")
llm = OpenAI(temperature=0.3, openai_api_key = "YOUR_OPENAI_API")

finding = LLMChain(llm=llm, prompt=qroler)
people = "USA"
answer = finding.run(people)
print(answer)