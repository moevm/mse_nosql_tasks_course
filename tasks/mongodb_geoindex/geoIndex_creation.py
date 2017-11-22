#!/usr/bin/python3


from pymongo import MongoClient, GEOSPHERE
import json

client = MongoClient()
db = client.my_db

#delete all from DB
client.drop_database('my_db')

doc = {
    "name": "Central Park",
   "location": { "type": "Point", "coordinates": [ -73.97, 40.77 ] },
   "category": "Parks"
}

#in order to create a collection
db.places.insert(doc)

