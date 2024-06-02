from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time

class Detection(BaseModel):
    cam_id: str
    detection: str
    name: str
    color: str
    license_num: str
    first_timestamp: time = Field(..., example="14:19:28")
    last_timestamp: time = Field(..., example="15:19:28")
    time: date

class DetectionQuery(BaseModel):
    cam_id: Optional[str] = None
    detection: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = None
    license_num: Optional[str] = None
    first_timestamp: Optional[time] = None
    last_timestamp: Optional[time] = None
    time: Optional[date] = None
