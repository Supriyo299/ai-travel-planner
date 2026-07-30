from app.models.trip import Trip
from app.models.user import User
from app.repositories.trip_repository import TripRepository
from app.schemas.trip import TripCreateRequest


class TripService:
    def __init__(self, db):
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
    ):
        return self.trip_repository.get_all_by_user(
            current_user.id
        )