from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
import os

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7)


prompt= PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']

    
)
parser= StrOutputParser()

joke_gen_chain= RunnableSequence(prompt,model,parser)
parallel_chain= RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count':RunnableLambda(lambda x: len(x.split()))
    }
)

final_chain= RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({'topic':'AI'})

final_res= """{}\n word count -""".format(result['joke'],result['word_count'])
print(final_res)