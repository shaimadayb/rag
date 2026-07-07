import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class Moderator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        with open("prompts/system_moderator.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def moderate(self, question):
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": self.system_prompt + "\n\nMessage: " + question}
            ]
        )
        text = response.choices[0].message.content.strip()
        if "unsafe" in text.lower() or "injection" in text.lower():
            return {"is_prompt_injection": True}
        return {"is_prompt_injection": False}