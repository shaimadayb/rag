import os
from groq import Groq
from dotenv import load_dotenv
from vector_db import VectorDB
from moderator import Moderator
from config import LLM_MODEL

load_dotenv()


class RAG:
    def __init__(self, chunks=None):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.db = VectorDB(chunks=chunks)
        self.moderator = Moderator()
        with open("prompts/system_rag.txt", "r", encoding="utf-8") as f:
            self.system_template = f.read()

    def answer_question(self, question):
        # Modération d'abord
        result = self.moderator.moderate(question)
        if result["is_prompt_injection"]:
            return "Je ne peux pas répondre à cette question."

        # Retrieval
        chunks, _ = self.db.retrieve(question, n=3)
        system_prompt = self.system_template.replace("{{Chunks}}", "\n".join(chunks))

        # Génération
        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content