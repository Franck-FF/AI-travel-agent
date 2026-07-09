from typing import List, Optional

from pydantic import BaseModel, Field


class TripRequest(BaseModel):
    destination: str = Field(
        min_length=2,
        description="Main travel destination."
    )

    duration_days: int = Field(
        ge=1,
        le=30,
        description="Number of days for the trip."
    )

    interests: List[str] = Field(
        min_length=1,
        description="User interests such as food, anime, museums."
    )

    budget: Optional[str] = Field(
        default=None,
        description="Budget level if provided."
    )

    travel_style: Optional[str] = Field(
        default=None,
        description="Travel style such as relaxed, luxury, budget, family."
    )


class DayPlan(BaseModel):
    day: int = Field(ge=1)
    theme: str = Field(min_length=2)
    area: str = Field(min_length=2)
    goal: str = Field(min_length=5)


class TripPlan(BaseModel):
    destination: str = Field(min_length=2)
    duration_days: int = Field(ge=1, le=30)
    days: List[DayPlan] = Field(min_length=1)


class VerifiedPlace(BaseModel):
    name: str = Field(min_length=2)
    category: str = Field(min_length=2)
    address: str = Field(min_length=2)
    opening_hours: str = Field(min_length=2)
    estimated_price: Optional[str] = None
    source_url: str = Field(min_length=5)
    verification_notes: str = Field(min_length=5)


class DayResearch(BaseModel):
    day: int = Field(ge=1)
    theme: str = Field(min_length=2)
    verified_places: List[VerifiedPlace] = Field(default_factory=list)


class ResearchResult(BaseModel):
    destination: str = Field(min_length=2)
    days: List[DayResearch] = Field(default_factory=list)