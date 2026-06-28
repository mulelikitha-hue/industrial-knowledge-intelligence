from utils.embeddings import create_embeddings


def retrieve_chunks(
    query,
    vector_store,
    top_k=3
):

    query_embedding = create_embeddings(
        [query]
    )

    results = vector_store.search(
        query_embedding,
        top_k
    )

    return results