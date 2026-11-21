from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
import os

model1= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7)




prompt1= PromptTemplate(
    template='Generate a joke about {topic}',
    input_variables=['topic']
)


prompt2= PromptTemplate(
    template='explain the following joke  {text}',
    input_variables=['text']
)
parser= StrOutputParser()



joke_gen_chain= RunnableSequence(prompt1,model1,parser)

parallel_chain= RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'explanation':RunnableSequence(prompt2, model1,parser)
    }
)

final_chain= RunnableSequence(joke_gen_chain, parallel_chain)
res= final_chain.invoke({'topic':'cricket'})
print(res)