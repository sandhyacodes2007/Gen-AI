from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
import os

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7)


prompt1= PromptTemplate(
    template= 'Write a detailed report on {topic}',
    input_variables=['topic']

)
prompt2= PromptTemplate(
template='Sumarize the following text \n {text}',
input_variables=['text']

)
parser= StrOutputParser()

report_gen_chain= prompt1 |model| parser
branch_chain= RunnableBranch(
(lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
RunnablePassthrough()
)

final_chain= RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukrain'}))