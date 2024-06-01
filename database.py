from pymongo import MongoClient
client = MongoClient("mongodb+srv://marcusmic01:2hTNwOncmYeytTZM@cluster0.tflek80.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.Intelligent_Camera

users_collection = db["detections"]
