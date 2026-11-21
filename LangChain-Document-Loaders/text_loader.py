from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=1.5)

prompt= PromptTemplate(
    template='Write a summary for the following poem-\n {topic}',
    input_variables=['topic']
)
parser= StrOutputParser

loader= TextLoader('cricket.txt',encoding='utf-8')
docs=loader.load()
print(docs)
print(type(docs))

print(docs[0])
print(len(docs))
print(docs[0].metadata)


chain= prompt |model |parser
chain.invoke({'poem':docs[0].page_content})