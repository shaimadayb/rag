from vector_db import VectorDB
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

chunks = [
    "Le chat bleu de Bob s'appelle Henri.",
    "La voiture rouge de Sarah roule à l'energie solaire.",
    "Le chien violet de Marc aboie en morse.",
    "La maison de Julie flotte au-dessus du sol.",
    "Le velo de Lea parle chinois."
]

db = VectorDB(chunks=chunks)
print("BASE CREEE")
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