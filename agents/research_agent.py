from schemas.trip_schema import DayResearch, ResearchResult, TripPlan, VerifiedPlace
from services.search_service import SearchService


class ResearchAgent:
    def __init__(self, search_service: SearchService):
        self.search_service = search_service

    def research_plan(self, trip_plan: TripPlan) -> ResearchResult:
        researched_days: list[DayResearch] = []

        for day in trip_plan.days:
            query = f"{day.area} {day.theme} {trip_plan.destination}"

            place_data = self.search_service.search_place(query)

            verified_place = VerifiedPlace(**place_data)

            day_research = DayResearch(
                day=day.day,
                theme=day.theme,
                verified_places=[verified_place],
            )

            researched_days.append(day_research)

        return ResearchResult(
            destination=trip_plan.destination,
            days=researched_days,
        )