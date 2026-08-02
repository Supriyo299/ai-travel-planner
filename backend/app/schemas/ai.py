from pydantic import BaseModel, Field


class GenerateTripRequest(BaseModel):
    destination: str = Field(min_length=2)
    budget: int = Field(gt=0)
    days: int = Field(gt=0)
    travel_style: str = Field(min_length=2)


class GenerateTripResponse(BaseModel):
    itinerary: str