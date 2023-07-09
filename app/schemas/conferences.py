from pydantic import BaseModel, constr, Field
from typing import Optional


time_validation = '\d{4}\/\d{2}\/\d{2}T\d{2}:\d{2}:\d{2}'


class Conference(BaseModel):
    id: Optional[int] = Field(read_only=True, allow_blank=True)
    title: str
    description: str
    start_time: constr(regex=time_validation)
    end_time: constr(regex=time_validation)
    Capacity: int
    items: str

    class Config:
        schema_extra = {
            "example": {
                "title": "some string",
                "description": "some string",
                "start_time": "1398/05/11T11:36:18",
                "end_time": "1398/05/11T11:26:14",
                "Capacity": 36,
                "items": "some string",
            }
        }

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "Capacity": self.Capacity,
            "items": self.items,
        }

