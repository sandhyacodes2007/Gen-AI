from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
import os
model1= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7)




prompt1= PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)


prompt2= PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)
parser= StrOutputParser()

parallel_chain= RunnableParallel({
    'tweet': RunnableSequence(prompt1,model1,parser),
    'linkedin':RunnableSequence(prompt2,model1,parser )
})
res= parallel_chain.invoke({'topic':'AI'})
print(res['tweet'])
print(res['linkedin'])