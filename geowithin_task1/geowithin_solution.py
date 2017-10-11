#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import json

client = MongoClient()
db = client.sw_db

result = list(db.places.find({'geometry':
                                {'$geoWithin':
                                    {'$geometry' : json.loads(open("polygon.json", "r").read())}
                                }
                            }
                     ))

open('correct_answer', 'w').write(str(len(result)))
client.drop_database('sw_db')
