
from fastapi import APIRouter, HTTPException
from app.models.car import CarRegistration, PositionUpdate, RouteRequest
from typing import Dict

router = APIRouter()

cars = {}

@router.post("/register_car")
def register_car(car: CarRegistration):
    if car.car_id in cars:
        raise HTTPException(status_code=400, detail="Car already registered")
    cars[car.car_id] = {"position": car.position, "speed": car.speed}
    return {"message": f"Car {car.car_id} registered successfully."}

@router.post("/update_position")
def update_position(update: PositionUpdate):
    if update.car_id not in cars:
        raise HTTPException(status_code=404, detail="Car not registered")

    car = cars[update.car_id]
    car["position"] = update.new_position
    car["speed"] = update.speed

    for other_id, other_car in cars.items():
        if other_id != update.car_id:
            distance = abs(other_car["position"] - car["position"])
            if distance < 100:
                return {
                    "collision_risk": True,
                    "message": f"Collision risk detected with car {other_id}."
                }
    return {"collision_risk": False}

@router.post("/map_route")
def map_route(route: RouteRequest):
    if route.source == "home" and route.destination == "office":
        return {"route": ["home", "raj watch house chauraha", "pathak petrol pump u turn", "rajeev plaza", "office"]}
    return {"route": [route.source, "Intermediate", route.destination]}
