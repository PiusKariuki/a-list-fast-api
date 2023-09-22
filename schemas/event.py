from pydantic import BaseModel, Field, FutureDatetime


class EventCreate(BaseModel):
    name: str = Field(..., min_length=8)
    start_time: FutureDatetime
    end_time: FutureDatetime