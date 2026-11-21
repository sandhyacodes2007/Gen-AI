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