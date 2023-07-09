from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "pass"
            }
        }

