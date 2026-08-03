from fastapi import APIRouter

from app.services.ai.gemini_service import GeminiService
from app.services.ai.ai_service import AIService

from app.schemas.ai import (
    GenerateTripRequest,
    GenerateTripResponse,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


# Existing endpoint (keep it)
@router.get("/test")
def test_ai():
    service = GeminiService()

    return {
        "response": service.test_connection()
    }


# New endpoint (add this)
@router.post(
    "/generate-trip",
    response_model=GenerateTripResponse,
)
def generate_trip(
    data: GenerateTripRequest,
):
    service = AIService()
    return service.generate_trip(data)