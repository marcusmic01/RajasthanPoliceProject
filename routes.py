from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from schema import *
from database import *
from typing import List
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/detection/")
def create_detection(detection: Detection):
    detection_data = jsonable_encoder(detection)
    # Convert time objects to strings in the format `HH:MM:SS`
    detection_data['first_timestamp'] = detection.first_timestamp.strftime('%H:%M:%S')
    detection_data['last_timestamp'] = detection.last_timestamp.strftime('%H:%M:%S')
    detection_data['time'] = detection.time.isoformat()

    result = users_collection.insert_one(detection_data)
    return {"inserted_id": str(result.inserted_id)}


# @router.get("/detection/", response_model=List[Detection])
# def search_detections(query: DetectionQuery = Depends()):
#     query_dict = {k: v for k, v in query.dict().items() if v is not None}
#     results = users_collection.find(query_dict)
#     return list(results)

@router.get("/detection/", response_model=List[Detection])
def search_detections(query: DetectionQuery = Depends()):
    query_dict = {k: v for k, v in query.dict().items() if v is not None}
    mongo_query = {}

    if 'first_timestamp' in query_dict and 'last_timestamp' in query_dict:
        mongo_query['first_timestamp'] = {"$gte": query.first_timestamp.strftime('%H:%M:%S')}
        mongo_query['last_timestamp'] = {"$lte": query.last_timestamp.strftime('%H:%M:%S')}
    else:
        if 'first_timestamp' in query_dict:
            mongo_query['first_timestamp'] = {"$gte": query.first_timestamp.strftime('%H:%M:%S')}
        if 'last_timestamp' in query_dict:
            mongo_query['last_timestamp'] = {"$lte": query.last_timestamp.strftime('%H:%M:%S')}

    if 'cam_id' in query_dict:
        mongo_query['cam_id'] = query.cam_id
    if 'detection' in query_dict:
        mongo_query['detection'] = query.detection
    if 'name' in query_dict:
        mongo_query['name'] = query.name
    if 'color' in query_dict:
        mongo_query['color'] = query.color
    if 'license_num' in query_dict:
        mongo_query['license_num'] = query.license_num
    if 'time' in query_dict:
        mongo_query['time'] = query.time.isoformat()

    results = list(users_collection.find(mongo_query))

    for result in results:
        result['first_timestamp'] = datetime.strptime(result['first_timestamp'], '%H:%M:%S').time()
        result['last_timestamp'] = datetime.strptime(result['last_timestamp'], '%H:%M:%S').time()
        result['time'] = datetime.fromisoformat(result['time']).date()

    return results