from typing import Optional

from pydantic import BaseModel, Field

from schemas.trip_schema import ResearchResult, TripPlan, TripRequest


class AgentState(BaseModel):
    user_request: str = Field(
        description="The original travel request written by the user."
    )

    trip_request: Optional[TripRequest] = Field(
        default=None,
        description="Structured trip details extracted by the intake agent.",
    )

    itinerary_plan: Optional[TripPlan] = Field(
        default=None,
        description="High-level itinerary plan created by the planning agent.",
    )

    research_results: Optional[ResearchResult] = Field(
        default=None,
        description="Destination research, activities, logistics, and recommendations.",
    )

    final_itinerary: Optional[str] = Field(
        default=None,
        description="Final polished travel itinerary written for the user.",
    )

    status: str = Field(
    default="success",
    description="Overall execution status of the workflow.",
    )

    errors: list[str] = Field(
        default_factory=list,
        description="Errors collected during graph execution.",
    )