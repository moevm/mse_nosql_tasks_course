from pymongo import MongoClient, GEOSPHERE
import json

client = MongoClient()
db = client.sw_db
db.places.create_index([('geometry', GEOSPHERE)])
lasers = json.load(open('lasers.json', 'r'))
db.places.insert_many(lasers)
