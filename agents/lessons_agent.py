from utils.answer_generator import answer_question


class LessonsLearnedAgent:

    def __init__(self, knowledge_agent):

        self.knowledge_agent = knowledge_agent

    def analyze(self, query):

        # ------------------------------------
        # Retrieve More Documents
        # ------------------------------------

        results = self.knowledge_agent.retrieve(

            query,

            top_k=25,

            rerank_top_k=5

        )

        # ------------------------------------
        # Keep only Historical Documents
        # ------------------------------------

        historical_categories = {

            "incident_report",

            "failure_report",

            "audit_report"

        }

        filtered_results = []

        for item in results:

            chunk = item["chunk"]

            if chunk["document_category"] in historical_categories:

                filtered_results.append(item)

        # ------------------------------------
        # If nothing found
        # ------------------------------------

        if len(filtered_results) == 0:

            return (

                "No incident reports, failure reports or audit reports related to this query were found in the uploaded documents.",

                []

            )

        # ------------------------------------
        # Build Context
        # ------------------------------------

        context = "\n\n".join(

            item["chunk"]["text"]

            for item in filtered_results

        )

        # ------------------------------------
        # Lessons Learned Prompt
        # ------------------------------------

        system_prompt = """
You are an Industrial Failure Intelligence Expert.

Using ONLY the retrieved historical documents, provide:

1. Similar Incidents
2. Root Causes
3. Lessons Learned
4. Preventive Actions
5. Future Recommendations

If the information is unavailable, clearly mention it.
"""

        answer = answer_question(

            system_prompt,

            query,

            context

        )

        return answer, filtered_results