
from fastapi import FastAPI
from app.routes.collision_route import router as collision_router
from app.routes.sign_detection import router as sign_router

app = FastAPI()

app.include_router(collision_router, prefix="/collision")
app.include_router(sign_router, prefix="/sign")

@app.get("/")
def read_root():
    return {"message": "Livis Car Safety System API is running"}
