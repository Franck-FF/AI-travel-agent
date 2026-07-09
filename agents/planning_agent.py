from schemas.trip_schema import TripRequest, TripPlan
from services.llm_service import LLMService


class PlanningAgent:
    def __init__(self, llm_service: LLMService):
        self.llm = llm_service

    def create_plan(self, trip_request: TripRequest) -> TripPlan:
        prompt = f"""
You are a high-level travel planning agent.

Create a day-by-day travel strategy.

Rules:
- Create exactly {trip_request.duration_days} days.
- Day numbers must start at 1.
- Each day needs a clear theme, area, and goal.
- Do not invent verified facts such as exact opening hours, prices, or schedules.

Trip request:
{trip_request.model_dump_json()}
"""

        return self.llm.generate_structured(
            prompt=prompt,
            response_model=TripPlan,
        )