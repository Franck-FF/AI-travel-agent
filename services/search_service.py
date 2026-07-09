class SearchService:
    def search_place(self, query: str) -> dict:
        return {
            "name": query,
            "category": "Needs real verification",
            "address": "To be verified",
            "opening_hours": "To be verified",
            "estimated_price": None,
            "source_url": "To be verified",
            "verification_notes": "Mock result only. Real web search will be added later."
        }