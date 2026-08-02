from app.schemas.ai import (
    GenerateTripRequest,
    GenerateTripResponse,
)
from app.services.ai.gemini_service import GeminiService


class AIService:
    def __init__(self):
        self.gemini = GeminiService()

    def generate_trip(
        self,
        data: GenerateTripRequest,
    ) -> GenerateTripResponse:

        return self.gemini.generate_trip(
            destination=data.destination,
            budget=data.budget,
            days=data.days,
            travel_style=data.travel_style,
        )