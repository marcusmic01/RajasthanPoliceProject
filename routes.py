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
    detection_data['first_timestamp'] = detection.first_timestamp.strftime('%H:%M:%S')
    detection_data['last_timestamp'] = detection.last_timestamp.strftime('%H:%M:%S')
    detection_data['time'] = detection.time.isoformat()

    result = users_collection.insert_one(detection_data)
    return {"inserted_id": str(result.inserted_id)}


# @router.post("/search_detections/", response_model=List[Detection])
# def search_detections(query: DetectionQuery):
#     mongo_query = {}

#     if query.cam_id:
#         mongo_query['cam_id'] = query.cam_id
#     if query.detection:
#         mongo_query['detection'] = query.detection
#     if query.name:
#         mongo_query['name'] = query.name
#     if query.color:
#         mongo_query['color'] = query.color
#     if query.license_num:
#         mongo_query['license_num'] = query.license_num
#     if query.first_timestamp:
#         mongo_query['first_timestamp'] = {"$gte": query.first_timestamp.strftime('%H:%M:%S')}
#     if query.last_timestamp:
#         mongo_query['last_timestamp'] = {"$lte": query.last_timestamp.strftime('%H:%M:%S')}
#     if query.time:
#         mongo_query['time'] = query.time.isoformat()

#     results = list(users_collection.find(mongo_query))
#     if not results:
#         raise HTTPException(status_code=404, detail="No detections found.")

#     for result in results:
#         result['id'] = str(result['_id'])
#         result['first_timestamp'] = result['first_timestamp']
#         result['last_timestamp'] = result['last_timestamp']
#         result['time'] = result['time']

#     return results

@router.post("/search_detections/", response_model=List[Detection])
def search_detections(query: DetectionQuery):
    print(f"Received query: {query.first_timestamp}, {query.last_timestamp}, {query.time}")
    mongo_query = {}

    if query.cam_id:
        mongo_query['cam_id'] = query.cam_id
    if query.detection:
        mongo_query['detection'] = query.detection
    if query.name:
        mongo_query['name'] = query.name
    if query.color:
        mongo_query['color'] = query.color
    if query.license_num:
        mongo_query['license_num'] = query.license_num
    if query.first_timestamp:
        mongo_query['first_timestamp'] = {"$gte": query.first_timestamp.strftime('%H:%M:%S')}
    if query.last_timestamp:
        mongo_query['last_timestamp'] = {"$lte": query.last_timestamp.strftime('%H:%M:%S')}
    if query.time:
        mongo_query['time'] = query.time.isoformat()

    results = list(users_collection.find(mongo_query))
    if not results:
        raise HTTPException(status_code=404, detail="No detections found.")

    for result in results:
        result['id'] = str(result['_id'])
        result['first_timestamp'] = result['first_timestamp']
        result['last_timestamp'] = result['last_timestamp']
        result['time'] = result['time']

    return results