from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001',dimensions=32)  # ← your supported model

documents=[
   "Delhi is the capital of India",
   "Kolkata is the capital of West Bengal",
"Paris is the capital of France"
]
res = embedding.embed_documents(documents)

print(str(res))