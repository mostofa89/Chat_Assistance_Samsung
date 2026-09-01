from app.chatbot.chatbot import answer_question as chatbot_answer_question


def answer_question(
    index,
    question,
    phones=None
):
    return chatbot_answer_question(
        index,
        question,
        phones
    )
