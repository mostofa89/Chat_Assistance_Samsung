from app.chatbot.llm import ask_llm
from app.rag.retriever import search


def answer_question(index, question):

    documents = search(index, question, k=3)

    context = "\n\n".join(documents)

    answer = ask_llm(
        context,
        question
    )

    return answer