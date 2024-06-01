from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from schema import *
from database import *
from typing import List

router = APIRouter()

@router.post("/detection/")
def create_user(detection: Detection):
    result = users_collection.insert_one(detection.dict())
    return {"inserted_id": str(result.inserted_id)} 

@router.get("/detection/", response_model=List[Detection])
def search_detections(query: DetectionQuery = Depends()):
    query_dict = {k: v for k, v in query.dict().items() if v is not None}
    results = users_collection.find(query_dict)
    return list(results)
