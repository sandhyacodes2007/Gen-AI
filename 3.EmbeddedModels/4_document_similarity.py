from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding= GoogleGenerativeAIEmbeddings(model= 'models/gemini-embedding-001',dimensions=300)

document=[
  " Virat Kohli is one of the greatest batsmen in cricket history.",
"Rohit Sharma is famous for hitting massive sixes in every match.",
"MS Dhoni is known for his calm and cool finishing in tough games.",
"Sachin Tendulkar scored one hundred centuries in international cricket.",
"Jasprit Bumrah is the best fast bowler in the current Indian team."
 ]

query= "tell  me about Jasprit Bumrah"

res_d= embedding.embed_documents(document)
res_q= embedding.embed_query(query)

scores= cosine_similarity([res_q], res_d)[0]

index, score= sorted(list(enumerate(scores)),key=lambda x:x[1] )[-1]

print(document[index])
print("similarity score is", score)
