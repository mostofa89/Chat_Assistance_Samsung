from app.chatbot.chatbot import ask_llm


class ReviewAgent:

    def generate_review(
        self,
        specifications
    ):

        context = f"""
Phone:
{specifications["phone"]}

Display:
{specifications["display"]}

Processor:
{specifications["processor"]}

RAM:
{specifications["ram"]}

Storage:
{specifications["storage"]}

Camera:
{specifications["camera"]}

Battery:
{specifications["battery"]}
"""

        question = """
Write a detailed but balanced
smartphone review based on these
specifications.

Include:

1. Display
2. Performance
3. Camera
4. Battery
5. Storage
6. Pros
7. Cons
8. Overall verdict
"""

        return ask_llm(
            context,
            question
        )