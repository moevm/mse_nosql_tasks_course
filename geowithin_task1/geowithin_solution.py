#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import json

client = MongoClient()
db = client.sw_db

result = db.places.find({'geometry':
                                {'$geoWithin':
                                    {'$geometry' : json.loads(open("polygon.json", "r").read())}
                                }
                            }
                     ).count()

open('correct_answer', 'w').write(str(result))
client.drop_database('sw_db')
