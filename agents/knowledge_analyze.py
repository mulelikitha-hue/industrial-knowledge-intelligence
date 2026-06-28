from utils.entity_extractor import extract_entities
from utils.graph_search import graph_search
from utils.retriever import retrieve_chunks
from utils.reranker import rerank_chunks
from utils.answer_generator import answer_question


class KnowledgeAgent:

    def __init__(self, kg, vector_store):

        self.kg = kg
        self.vector_store = vector_store

    # --------------------------------------------------
    # Retrieval Pipeline
    # --------------------------------------------------

    def retrieve(self, query,top_k=10,
    rerank_top_k=3):

        # Graph Search
        question_entities = extract_entities(query)

        graph_results = graph_search(
            question_entities,
            self.kg
        )

        # FAISS Retrieval
        faiss_results = retrieve_chunks(
            query=query,
            vector_store=self.vector_store,
            top_k=top_k
        )

        # Merge Results
        merged_results = []

        seen_chunk_ids = set()

        for chunk in graph_results:

            if chunk["chunk_id"] not in seen_chunk_ids:

                merged_results.append({

                    "chunk": chunk,

                    "faiss_score": 1.0

                })

                seen_chunk_ids.add(
                    chunk["chunk_id"]
                )

        for item in faiss_results:

            chunk = item["chunk"]

            if chunk["chunk_id"] not in seen_chunk_ids:

                merged_results.append(item)

                seen_chunk_ids.add(
                    chunk["chunk_id"]
                )

        # CrossEncoder Reranking
        results = rerank_chunks(
            query,
            merged_results,
            top_k=3,
            top_k=rerank_top_k
        )

        return results

    # --------------------------------------------------
    # General Question Answering
    # --------------------------------------------------

    def analyze(self, query):

        results = self.retrieve(query)

        context = "\n\n".join(

            item["chunk"]["text"]

            for item in results

        )

        system_prompt = """
        You are an Industrial Knowledge Assistant.

        Answer using ONLY the retrieved documents.

        Provide:

        1. Answer
        2. Source Evidence
        3. Confidence Score
        """

        answer = answer_question(

            system_prompt,

            query,

            context

        )

        return answer, results