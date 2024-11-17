
# Car Safety System API

## Overview

This project demonstrates a dummy working of a car safety system using FastAPI. 
It includes the following features:
1. **Collision Detection** using wireless communication between cars.
2. **Route Mapping** based on frequent following paths.
3. **Signboard Detection** using image processing with OpenCV and NLP to alert the driver if a speed limit or relevant sign is detected.

## Folder Structure

```
CarSafetySystem/
│
├── main.py                 # Main entry point for the FastAPI application
├── requirements.txt        # Python package dependencies
└── app/
    ├── models/
    │   └── car.py          # Pydantic models for car registration, updates, and sign detection
    ├── routes/
    │   ├── collision_route.py # APIs for collision detection and route mapping
    │   └── sign_detection.py  # API for signboard detection using image processing
    └── utils/
        └── image_processing.py # Utility functions for image processing using OpenCV and Tesseract
```

## Installation

### Prerequisites

- Python 3.8 or above
- `pip` for managing Python packages

### Steps

1. Clone the repository or extract the zip file.
2. Navigate to the project directory:
   ```bash
   cd CarSafetySystem
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## API Endpoints

### 1. Register a Car
**Endpoint**: `/collision/register_car`  
**Method**: `POST`  
**Payload**:
```json
{
    "car_id": "car1",
    "position": 0,
    "speed": 60
}
```

### 2. Update Car Position
**Endpoint**: `/collision/update_position`  
**Method**: `POST`  
**Payload**:
```json
{
    "car_id": "car1",
    "new_position": 500,
    "speed": 40
}
```

### 3. Map Route
**Endpoint**: `/collision/map_route`  
**Method**: `POST`  
**Payload**:
```json
{
    "source": "A",
    "destination": "B"
}
```

### 4. Detect Signboard
**Endpoint**: `/sign/detect_sign`  
**Method**: `POST`  
**Payload**:
```json
{
    "image_path": "path/to/sign_image.jpg"
}
```

## Additional Information

- The sign detection API uses OpenCV and Tesseract OCR for text recognition from the image.
- The `detect_sign` function reads the signboard text and alerts if a speed limit is detected.

## Tech Stack

- **FastAPI**: For building the RESTful APIs
- **Pydantic**: For data validation
- **OpenCV**: For image processing
- **Tesseract**: For Optical Character Recognition (OCR)

## License

This project is for educational purposes and demonstration only.
