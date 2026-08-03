from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    UserLoginRequest,
    UserRegisterRequest,
)

class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register_user(self, data: UserRegisterRequest) -> User:
        existing_user = self.user_repository.get_by_email(data.email)

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            full_name=data.full_name,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        return self.user_repository.create(user)

    def login_user(self, data: UserLoginRequest) -> str:
        user = self.user_repository.get_by_email(data.email)

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            data.password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        return create_access_token(
            subject=str(user.id),
        )