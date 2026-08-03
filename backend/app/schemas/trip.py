from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TripCreateRequest(BaseModel):
    destination: str = Field(
        min_length=2,
        max_length=150,
    )

    budget: int = Field(
        gt=0,
    )

    days: int = Field(
        gt=0,
    )

    travel_style: str = Field(
        min_length=2,
        max_length=50,
    )


class TripResponse(BaseModel):
    id: UUID
    destination: str
    budget: int
    days: int
    travel_style: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
class TripUpdateRequest(BaseModel):
    destination: str
    budget: int
    days: int
    travel_style: str