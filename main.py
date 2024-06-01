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

app = FastAPI()

app.include_router(router)
