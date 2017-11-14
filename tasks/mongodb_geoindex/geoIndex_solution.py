#!/usr/bin/python3


from pymongo import MongoClient, GEOSPHERE

client = MongoClient()
db = client.my_db

db.places.create_index([('location', GEOSPHERE)])
