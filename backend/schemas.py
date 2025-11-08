from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Contact(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=5000)
    source: Optional[str] = Field(default="website")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "message": "Bonjour, j’aimerais un site vitrine pour mon activité.",
                "source": "website",
            }
        }
