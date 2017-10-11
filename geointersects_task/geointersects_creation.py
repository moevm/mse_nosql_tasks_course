#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import json

client = MongoClient()
db = client.sw_db

#удаляем все объекты из БД
client.drop_database('sw_db')
db.places.create_index([('geometry', GEOSPHERE)])
polygons = json.load(open('manypolygons.json', 'r'))
db.places.insert_many(polygons)
