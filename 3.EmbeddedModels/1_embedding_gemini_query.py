from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001',dimensions=32)  # ← your supported model

res = embedding.embed_query("Delhi is the capital of India")

print(str(res))