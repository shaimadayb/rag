import csv
from vector_db import VectorDB
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

chunks = []
with open("05_corpus_rag.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        chunks.append(row["text"])

db = VectorDB(chunks=chunks)
chunks_result, _ = db.retrieve("Quelle est la couleur du chat de Bob ?")
print("CHUNKS:", chunks_result)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "Réponds uniquement à partir de ces infos : " + "\n".join(chunks_result)},
        {"role": "user", "content": "Quelle est la couleur du chat de Bob ?"}
    ]
)
print(response.choices[0].message.content)