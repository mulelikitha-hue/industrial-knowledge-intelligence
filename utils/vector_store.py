import faiss
import numpy as np


class VectorStore:

    def __init__(self, embedding_dimension):

        self.index = faiss.IndexFlatIP(embedding_dimension)

        self.chunk_metadata = []

    def add_documents(self, embeddings, chunks):

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        self.index.add(embeddings)

        self.chunk_metadata.extend(chunks)

    def search(self, query_embedding, top_k=3):

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(distances[0], indices[0]):

            if idx < len(self.chunk_metadata):

                results.append({

                    "chunk": self.chunk_metadata[idx],

                    "faiss_score": float(score)

                })

        return results