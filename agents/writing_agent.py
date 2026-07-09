from schemas.trip_schema import ResearchResult
from services.llm_service import LLMService


class WritingAgent:
    def __init__(self, llm_service: LLMService):
        self.llm = llm_service

    def write_itinerary(self, research_result: ResearchResult) -> str:
        prompt = f"""
You are an expert luxury travel writer.

Your job is to transform structured travel research into a beautiful,
easy-to-read Markdown itinerary.

Requirements:

- Write professional Markdown.
- Use headings for each day.
- Briefly introduce each day.
- Present each verified place clearly.
- Include address, opening hours, estimated price and source.
- Add practical travel tips when appropriate.
- Do NOT invent facts that are not present.
- If information is "To be verified", mention that naturally.

Travel research:

{research_result.model_dump_json(indent=2)}
"""

        return self.llm.generate_text(prompt)