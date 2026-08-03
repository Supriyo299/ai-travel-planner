from fastapi import APIRouter, Depends, status
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
    status_code=status.HTTP_201_CREATED,
)
def create_trip(
    data: TripCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TripService(db)

    return service.create_trip(
        current_user=current_user,
        data=data,
    )


@router.get(
    "",
    response_model=list[TripResponse],
)
def get_my_trips(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TripService(db)

    return service.get_my_trips(
        current_user=current_user,
    )