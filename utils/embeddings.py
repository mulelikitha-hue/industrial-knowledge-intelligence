from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts):
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )
    return np.array(embeddings).astype("float32")