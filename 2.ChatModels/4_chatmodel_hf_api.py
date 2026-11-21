from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")  # ← change 'huggingfacehub_api_token' to 'token'
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("what is the capital of India")
print(res.content)