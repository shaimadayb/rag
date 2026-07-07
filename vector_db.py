import chromadb
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, CHROMA_PATH, COLLECTION_NAME


class VectorDB:
    def __init__(self, chunks=None):
        self.client = chromadb.PersistentClient(path=CHROMA_PATH)
        existing_collections = [c.name for c in self.client.list_collections()]

        if COLLECTION_NAME in existing_collections:
            self.collection = self.client.get_collection(COLLECTION_NAME)
            model_name = self.collection.metadata["embedding_model"]
            self.model = SentenceTransformer(model_name)

        elif chunks is not None:
            self.model = SentenceTransformer(EMBEDDING_MODEL)
            self.collection = self.client.create_collection(
                name=COLLECTION_NAME,
                metadata={"embedding_model": EMBEDDING_MODEL}
            )
            embeddings = self.encode(chunks)
            ids = [str(i) for i in range(len(chunks))]
            metadatas = [{"source": "corpus"} for _ in chunks]
            self.collection.add(
                ids=ids,
                documents=chunks,
                embeddings=embeddings,
                metadatas=metadatas
            )

        else:
            raise ValueError("Aucune base existante et aucun chunk fourni.")

    def encode(self, texts):
        return self.model.encode(texts, normalize_embeddings=True, show_progress_bar=True).tolist()

    def retrieve(self, question, n=3):
        question_embedding = self.encode([question])
        results = self.collection.query(
            query_embeddings=question_embedding,
            n_results=n
        )
        print("DEBUG results:", results)
        return results["documents"][0], results["metadatas"][0]