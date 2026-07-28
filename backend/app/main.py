from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.router import api_router
from app.api.dependencies import get_db
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "AI Travel Planner API is running 🚀",
        "environment": settings.APP_ENV,
    }


@app.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {
        "status": "healthy",
        "database": "connected",
    }