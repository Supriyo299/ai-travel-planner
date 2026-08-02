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
        return response.text 