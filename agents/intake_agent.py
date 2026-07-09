from schemas.trip_schema import TripRequest
from services.llm_service import LLMService


class TripIntakeAgent:
    def __init__(self, llm_service: LLMService):
        self.llm = llm_service

    def parse_user_request(self, user_prompt: str) -> TripRequest:
        prompt = f"""
You extract structured travel information from user travel requests.

Rules:
- Extract the main destination.
- Extract the number of travel days.
- Extract user interests as a list.
- If budget is missing, leave it as null.
- If travel style is missing, leave it as null.

User request:
{user_prompt}
"""

        return self.llm.generate_structured(
            prompt=prompt,
            response_model=TripRequest,
        )