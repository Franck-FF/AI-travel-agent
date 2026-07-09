from typing import Type, TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.settings import settings

T = TypeVar("T", bound=BaseModel)


class LLMService:
    """
    Central service for all OpenAI interactions.

    Supports:
    - Normal text generation
    - Structured Pydantic outputs
    """

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    def generate_text(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text

    def generate_structured(
        self,
        prompt: str,
        response_model: Type[T],
    ) -> T:
        """
        Generate a validated Pydantic object directly.
        """

        response = self.client.responses.parse(
            model=self.model,
            input=prompt,
            text_format=response_model,
        )

        return response.output_parsed