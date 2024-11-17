from fastapi import APIRouter, HTTPException
from app.models.car import SignDetectionRequest
from app.utils.image_processing import *

router = APIRouter()

@router.post("/detect_sign")
def detect_signboard(request: SignDetectionRequest):
    try:
        image_url = request.image_url
        
        sign_text = extract_text(image_url)
        print(sign_text)
        if sign_text:
            return {"alert": True, "message": f"follow: {sign_text}"}
        return {"alert": False, "message": "No significant sign detected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
