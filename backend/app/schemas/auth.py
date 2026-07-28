from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegisterRequest(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=100,
        description="User's full name",
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password",
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "full_name": "Jeet Das",
                "email": "jeet@example.com",
                "password": "MyStrongPassword123!",
            }
        }
    )