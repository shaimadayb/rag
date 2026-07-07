"""Boucle interactive pour tester le RAG en ligne de commande."""
import csv
from rag import RAG

# Charger le corpus
chunks = []
with open("05_corpus_rag.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        chunks.append(row["text"])

rag = RAG(chunks=chunks)
print("Pose ta question (ligne vide pour quitter).")

while True:
    question = input("\n> ").strip()
    if not question:
        break
    print(rag.answer_question(question))