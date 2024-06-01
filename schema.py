from pydantic import BaseModel
from typing import List, Optional

class Detection(BaseModel):
    cam_id: str
    detection: str
    name: str
    color: str
    license_num: int
    first_timestamp: str
    last_timestamp : str

class DetectionQuery(BaseModel):
    cam_id: Optional[str] = None
    detection: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = None
    license_num: Optional[int] = None
    first_timestamp: Optional[str] = None
    last_timestamp: Optional[str] = None
