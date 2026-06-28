from utils.answer_generator import answer_question


class MaintenanceAgent:

    def __init__(self, knowledge_agent):

        self.knowledge_agent = knowledge_agent

    def analyze(self, query):

        # -------------------------------
        # Retrieve Relevant Chunks
        # -------------------------------

        results = self.knowledge_agent.retrieve(query, top_k=10,
    rerank_top_k=3)

        # -------------------------------
        # Build Context
        # -------------------------------

        context = "\n\n".join(

            item["chunk"]["text"]

            for item in results

        )

        # -------------------------------
        # Maintenance Prompt
        # -------------------------------

        maintenance_prompt = f"""
You are an Industrial Maintenance Engineer.

Using ONLY the retrieved documents, answer in the following format:

1. Possible Root Cause
2. Inspection Steps
3. Recommended Maintenance Actions
4. Preventive Maintenance Recommendations

Question:
{query}
"""

        maintenance_answer = answer_question(

            maintenance_prompt,

            query,

            context

        )

        return maintenance_answer, results