from .specification_agent import SpecificationAgent
from .review_agent import (
    ReviewAgent,
    calculate_gsmarena_overall_score,
    extract_overall_score,
)


class PhoneReviewCrew:

    def __init__(self, db):
        self.spec_agent = SpecificationAgent(db)
        self.review_agent = ReviewAgent()

    def run(self, phone):

        specifications = self.spec_agent.get_specification(phone)

        review = self.review_agent.generate_review(
            specifications
        )

        overall_score, category_scores = calculate_gsmarena_overall_score(
            specifications
        )

        return {
            "specifications": specifications,
            "review": review,
            "overall_score": extract_overall_score(review) or overall_score,
            "category_scores": category_scores
        }
