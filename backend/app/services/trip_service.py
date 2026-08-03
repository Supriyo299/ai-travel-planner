from uuid import UUID
from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.models.user import User
from app.repositories.trip_repository import TripRepository
from app.schemas.trip import TripCreateRequest, TripUpdateRequest


class TripService:
    def __init__(self, db: Session):
        self.trip_repository = TripRepository(db)

    def create_trip(
        self,
        current_user: User,
        data: TripCreateRequest,
    ) -> Trip:
        trip = Trip(
            user_id=current_user.id,
            destination=data.destination,
            budget=data.budget,
            days=data.days,
            travel_style=data.travel_style,
        )

        return self.trip_repository.create(trip)

    def get_my_trips(
        self,
        current_user: User,
    ) -> list[Trip]:
        return self.trip_repository.get_all_by_user(current_user.id)

    def get_trip(
        self,
        current_user: User,
        trip_id: UUID,
    ) -> Trip:
        trip = self.trip_repository.get_by_id(trip_id)

        if trip is None:
            raise ValueError("Trip not found")

        if trip.user_id != current_user.id:
            raise ValueError("Unauthorized")

        return trip

    def update_trip(
        self,
        trip_id: UUID,
        current_user: User,
        data: TripUpdateRequest,
    ) -> Trip:
        trip = self.trip_repository.get_by_id(trip_id)

        if trip is None:
            raise ValueError("Trip not found")

        if trip.user_id != current_user.id:
            raise ValueError("Unauthorized")

        trip.destination = data.destination
        trip.budget = data.budget
        trip.days = data.days
        trip.travel_style = data.travel_style

        print("\n===== UPDATE DEBUG =====")
        print("Request Data:", data)
        print("Destination:", trip.destination)
        print("Budget:", trip.budget)
        print("Days:", trip.days)
        print("Travel Style:", trip.travel_style)
        print("========================\n")

        return self.trip_repository.update(trip)

    def delete_trip(
        self,
        trip_id: UUID,
        current_user: User,
    ) -> None:

        trip = self.trip_repository.get_by_id(trip_id)

        if trip is None:
            raise ValueError("Trip not found")

        if trip.user_id != current_user.id:
            raise ValueError("Unauthorized")

        self.trip_repository.delete(trip)