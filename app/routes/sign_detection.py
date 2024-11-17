from fastapi import APIRouter, HTTPException
from app.models.car import SignDetectionRequest
from app.utils.image_processing import *

router = APIRouter()

@router.post("/detect_sign")
def detect_signboard(request: SignDetectionRequest):
    try:
        image_url = request.image_url
        local_image_path = "downloaded_image.jpg"
        

        download_image(image_url, local_image_path)
        sign_text = extract_text_from_image(local_image_path)
        print(sign_text)
        if sign_text:
            return {"alert": True, "message": f"follow: {sign_text}"}
        return {"alert": False, "message": "No significant sign detected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
