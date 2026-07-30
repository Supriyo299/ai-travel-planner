from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.trip import Trip


class TripRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, trip: Trip) -> Trip:
        self.db.add(trip)
        self.db.commit()
        self.db.refresh(trip)
        return trip

    def get_all_by_user(self, user_id: UUID) -> list[Trip]:
        statement = (
            select(Trip)
            .where(Trip.user_id == user_id)
            .order_by(Trip.created_at.desc())
        )

        return list(self.db.scalars(statement).all())