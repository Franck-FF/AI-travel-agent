from agents.intake_agent import TripIntakeAgent
from agents.planning_agent import PlanningAgent
from agents.research_agent import ResearchAgent
from agents.writing_agent import WritingAgent
from graph.state import AgentState
from graph.travel_graph import build_travel_graph
from services.llm_service import LLMService
from services.search_service import SearchService


class TravelPlannerService:
    """
    Orchestrates the LangGraph workflow.

    This service is responsible only for generating travel plans.
    It does not decide how results are displayed or saved.
    """

    def __init__(self):
        llm_service = LLMService()
        search_service = SearchService()

        intake_agent = TripIntakeAgent(llm_service)
        planning_agent = PlanningAgent(llm_service)
        research_agent = ResearchAgent(search_service)
        writing_agent = WritingAgent(llm_service)

        self.graph = build_travel_graph(
            intake_agent=intake_agent,
            planning_agent=planning_agent,
            research_agent=research_agent,
            writing_agent=writing_agent,
        )

    def generate_itinerary(self, user_request: str) -> AgentState:
        initial_state = AgentState(
            user_request=user_request
        )

        return self.graph.invoke(initial_state)