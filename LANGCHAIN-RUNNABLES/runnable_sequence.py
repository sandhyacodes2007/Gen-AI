from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7)



prompt1= PromptTemplate(
    template= 'Write a joke about {topic}',
    input_variables= ['topic']
)

parser= StrOutputParser()


prompt2= PromptTemplate(
    template= 'Write the following joke  {text}',
    input_variables= ['text']
)

chain= RunnableSequence(prompt1,model, parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))