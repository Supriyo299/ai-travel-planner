from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.trip import (
    TripCreateRequest,
    TripUpdateRequest,
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

@router.get(
    "/{trip_id}",
    response_model=TripResponse,
)
def get_trip(
    trip_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = TripService(db)

    try:
        return service.get_trip(
            current_user,
            trip_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

@router.put(
    "/{trip_id}",
    response_model=TripResponse,
)
def update_trip(
    trip_id: UUID,
    data: TripUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = TripService(db)

    try:
        return service.update_trip(
            trip_id=trip_id,
            current_user=current_user,
            data=data,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@router.delete(
    "/{trip_id}",
    status_code=204,
)
def delete_trip(
    trip_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = TripService(db)

    try:
        service.delete_trip(
            trip_id=trip_id,
            current_user=current_user,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )