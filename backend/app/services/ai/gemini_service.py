from google import genai
from app.core.config import settings


class GeminiService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def test_connection(self):
        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents="Say hello in one sentence."
        )
    def generate_trip(
        self,
        destination: str,
        budget: int,
        days: int,
        travel_style: str,
    ) -> str:

        prompt = f"""
You are a professional travel planner.

Create a detailed {days}-day itinerary.

Destination: {destination}
Budget: ₹{budget}
Travel Style: {travel_style}

Include:
- Day-wise itinerary
- Hotel suggestions
- Food recommendations
- Local transportation
- Estimated expenses
- Packing list
- Travel tips

Format the response neatly.
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text