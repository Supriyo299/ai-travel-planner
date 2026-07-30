from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.trip import (
    TripCreateRequest,
    TripResponse,
)
from app.services.trip_service import TripService

router = APIRouter(
    prefix="/trips",
    tags=["Trips"],
)


@router.post(
    "",
    response_model=TripResponse,
)
def create_trip(
    data: TripCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = TripService(db)
    return service.create_trip(current_user, data)


@router.get(
    "",
    response_model=List[TripResponse],
)
def get_my_trips(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = TripService(db)
    return service.get_my_trips(current_user)