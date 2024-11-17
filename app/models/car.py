
from pydantic import BaseModel

class CarRegistration(BaseModel):
    car_id: str
    position: str
    speed: float

class PositionUpdate(BaseModel):
    car_id: str
    new_position: float
    speed: float

class RouteRequest(BaseModel):
    source: str
    destination: str

class SignDetectionRequest(BaseModel):
    image_url: str
