import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

# OpenAI
# os.environ["OPENAI_API_KEY"] = "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"
# Oh
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_API_BASE"] = "https://aigptx.top/v1"

from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
# Feetful of Fun

from langchain.prompts import PromptTemplate
 
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)