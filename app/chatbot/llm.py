import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(context, question):

    prompt = f"""
You are a Samsung smartphone assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"The information is not available in the database."

Context:

{context}

Question:

{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]