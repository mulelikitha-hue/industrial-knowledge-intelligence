import ollama


def answer_question(
    system_prompt,
    query,
    context
):

    prompt = f"""
{system_prompt}

Use ONLY the information provided in the context.

If the answer is not present in the context, clearly say that the information is unavailable.

-------------------------
CONTEXT
-------------------------
{context}

-------------------------
QUESTION
-------------------------
{query}
"""

    response = ollama.chat(

        model="mistral",

        messages=[

            {

                "role": "user",

                "content": prompt

            }

        ]

    )

    return response["message"]["content"]