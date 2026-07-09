import logging
from collections.abc import Callable

from langgraph.graph import END, StateGraph

from agents.intake_agent import TripIntakeAgent
from agents.planning_agent import PlanningAgent
from agents.research_agent import ResearchAgent
from agents.writing_agent import WritingAgent
from graph.state import AgentState


logger = logging.getLogger(__name__)


def build_travel_graph(
    intake_agent: TripIntakeAgent,
    planning_agent: PlanningAgent,
    research_agent: ResearchAgent,
    writing_agent: WritingAgent,
):
    def execute_node(
        node_name: str,
        state: AgentState,
        action: Callable[[], None],
    ) -> AgentState:
        if state.status == "failed":
            logger.warning("%s node skipped because workflow already failed", node_name)
            return state

        logger.info("%s node started", node_name)

        try:
            action()
            logger.info("%s node completed", node_name)

        except Exception as error:
            logger.exception("%s node failed", node_name)
            state.status = "failed"
            state.errors.append(f"{node_name} node failed: {error}")

        return state

    def intake_node(state: AgentState) -> AgentState:
        def action() -> None:
            state.trip_request = intake_agent.parse_user_request(state.user_request)

        return execute_node("Intake", state, action)

    def planning_node(state: AgentState) -> AgentState:
        def action() -> None:
            state.itinerary_plan = planning_agent.create_plan(state.trip_request)

        return execute_node("Planning", state, action)

    def research_node(state: AgentState) -> AgentState:
        def action() -> None:
            state.research_results = research_agent.research_plan(state.itinerary_plan)

        return execute_node("Research", state, action)

    def writing_node(state: AgentState) -> AgentState:
        def action() -> None:
            state.final_itinerary = writing_agent.write_itinerary(state.research_results)

        return execute_node("Writing", state, action)

    graph = StateGraph(AgentState)

    graph.add_node("intake", intake_node)
    graph.add_node("planning", planning_node)
    graph.add_node("research", research_node)
    graph.add_node("writing", writing_node)

    graph.set_entry_point("intake")

    graph.add_edge("intake", "planning")
    graph.add_edge("planning", "research")
    graph.add_edge("research", "writing")
    graph.add_edge("writing", END)

    return graph.compile()