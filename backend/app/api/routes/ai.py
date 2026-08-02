from fastapi import APIRouter

from app.services.ai.gemini_service import GeminiService

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.get("/test")
def test_ai():
    service = GeminiService()

    return {
        "response": service.test_connection()
    }