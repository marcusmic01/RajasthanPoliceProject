# from fastapi import FastAPI

# app = FastAPI()



# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://marcusmic01:2hTNwOncmYeytTZM@cluster0.tflek80.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware

from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from schema import *
from database import *
from typing import List
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from datetime import datetime

app = FastAPI()



# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:5173",
#     "http://127.0.0.1:8000",
#     "http://127.0.0.1:5500"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.options("/search_detections/")
async def options_search_detections():
    return {"allow-origin": "*", "allow-methods": "*", "allow-headers": "*"} 

app.include_router(router)
