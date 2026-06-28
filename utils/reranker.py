from sentence_transformers import CrossEncoder

# Load the CrossEncoder model only once
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_chunks(query, retrieved_chunks, top_k=3):

    pairs = []

    # Create (query, chunk) pairs
    for item in retrieved_chunks:

        pairs.append(
            [query, item["chunk"]["text"]]
        )

    # Predict relevance scores
    scores = model.predict(pairs)

    scored_chunks = []

    # Store FAISS score + CrossEncoder score + Chunk
    for score, item in zip(scores, retrieved_chunks):

        scored_chunks.append({

            "chunk": item["chunk"],

            "faiss_score": item["faiss_score"],

            "reranker_score": float(score)

        })

    # Sort using CrossEncoder score
    scored_chunks.sort(
        key=lambda x: x["reranker_score"],
        reverse=True
    )

    # Return top-k
    return scored_chunks[:top_k]