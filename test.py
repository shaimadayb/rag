from vector_db import VectorDB

db = VectorDB(chunks=["Le chat bleu de Bob sappelle Henri", "La voiture de Sarah est rouge"])
print("count:", db.collection.count())
r = db.retrieve("chat Bob", n=2)
print("result:", r)
