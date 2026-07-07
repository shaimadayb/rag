from vector_db import VectorDB

chunks = [
    "Le chat bleu de Bob s'appelle Henri.",
    "La voiture rouge de Sarah roule à l'energie solaire.",
    "Le chien violet de Marc aboie en morse.",
    "La maison de Julie flotte au-dessus du sol.",
    "Le velo de Lea parle chinois."
]

db = VectorDB(chunks=chunks)
print("BASE CREEE")
docs, metas = db.retrieve("Quelle est la couleur du chat de Bob ?")
print("RESULTAT:", docs)