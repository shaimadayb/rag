from rag import RAG

chunks = [
    "Le chat bleu de Bob s'appelle Henri.",
    "La voiture rouge de Sarah roule à l'energie solaire.",
    "Le chien violet de Marc aboie en morse.",
    "La maison de Julie flotte au-dessus du sol.",
    "Le velo de Lea parle chinois."
]

rag = RAG(chunks=chunks)
print(rag.answer_question("Quelle est la couleur du chat de Bob ?"))