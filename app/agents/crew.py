from .specification_agent import SpecificationAgent
from .review_agent import ReviewAgent


class SamsungCrew:

    def __init__(self, db):

        self.spec_agent = (
            SpecificationAgent(db)
        )

        self.review_agent = (
            ReviewAgent()
        )


    def generate_review(self, phone):

        specifications = (
            self.spec_agent
            .get_specification(phone)
        )

        review = (
            self.review_agent
            .generate_review(
                specifications
            )
        )

        return review