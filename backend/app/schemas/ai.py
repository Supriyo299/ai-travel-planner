from pydantic import BaseModel, Field


class GenerateTripRequest(BaseModel):
    destination: str = Field(min_length=2)
    budget: int = Field(gt=0)
    days: int = Field(gt=0)
    travel_style: str = Field(min_length=2)


class DayPlan(BaseModel):
    day: int
    title: str
    activities: list[str]


class Hotel(BaseModel):
    name: str
    price_per_night: str


class BudgetItem(BaseModel):
    category: str
    amount: int


class GenerateTripResponse(BaseModel):
    destination: str
    summary: str

    itinerary: list[DayPlan]

    hotels: list[Hotel]

    food_recommendations: list[str]

    transportation: list[str]

    packing_list: list[str]

    budget_breakdown: list[BudgetItem]

    travel_tips: list[str]