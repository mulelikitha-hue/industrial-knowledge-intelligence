import ollama


def classify_query(query):

    system_prompt = """
You are an AI Router for an Industrial Knowledge Intelligence Platform.

Classify the user's question into EXACTLY ONE category.

Possible outputs:

knowledge
maintenance
compliance
lessons_learned

Rules:

- General document questions -> knowledge
- Equipment failures, repairs, inspections, maintenance, root cause -> maintenance
- Regulations, standards, ISO, OISD, Factory Act, audits -> compliance
- Previous incidents, failure history, lessons learned, near misses -> lessons_learned

Return ONLY one word.
"""

    response = ollama.chat(

        model="mistral",

        messages=[

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": query
            }

        ]

    )

    return response["message"]["content"].strip().lower()