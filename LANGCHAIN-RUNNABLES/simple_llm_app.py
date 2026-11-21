from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7)

prompt= PromptTemplate(
    input_variables=['topic']
    template='Suggest a catchy blog title about {topic}',
   
)


#create an LLMChain

chain= LLMChain(model=model, prompt=prompt)
parser= StrOutputParser()

chain= prompt | model|parser
result= chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()