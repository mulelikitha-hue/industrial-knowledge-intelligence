from utils.answer_generator import answer_question


class ComplianceAgent:

    def __init__(self, knowledge_agent):

        self.knowledge_agent = knowledge_agent

    def analyze(self, query):

        # ------------------------------------
        # Retrieve Relevant Chunks
        # ------------------------------------

        results = self.knowledge_agent.retrieve(query, top_k=10,
    rerank_top_k=3)

        # ------------------------------------
        # Build Context
        # ------------------------------------

        context = "\n\n".join(

            item["chunk"]["text"]

            for item in results

        )

        # ------------------------------------
        # Compliance Prompt
        # ------------------------------------

        compliance_prompt = f"""
You are an Industrial Compliance Expert.

Using ONLY the retrieved documents, answer in the following format:

1. Applicable Standards
2. Compliance Status
3. Compliance Gaps
4. Risks
5. Recommended Corrective Actions

If the documents do not contain enough information, clearly mention it.

Question:
{query}
"""

        answer = answer_question(

            compliance_prompt,

            query,

            context

        )

        return answer, results