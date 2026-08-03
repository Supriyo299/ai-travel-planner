from google import genai
from app.core.config import settings
from app.schemas.ai import GenerateTripResponse

class GeminiService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_trip(
        self,
        destination: str,
        budget: int,
        days: int,
        travel_style: str,
    ) -> GenerateTripResponse:

        prompt = f"""
You are an expert travel planner.

Generate a travel itinerary.

Destination: {destination}
Budget: ₹{budget}
Days: {days}
Travel Style: {travel_style}

Return the result matching this schema:

- destination
- summary
- itinerary
    - day
    - title
    - activities
- hotels
    - name
    - price_per_night
- food_recommendations
- transportation
- packing_list
- budget_breakdown
    - category
    - amount
- travel_tips

Do NOT return markdown.
Do NOT wrap the response in ```json.
Return valid JSON only.
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": GenerateTripResponse,
            },
        )

        return response.parsed