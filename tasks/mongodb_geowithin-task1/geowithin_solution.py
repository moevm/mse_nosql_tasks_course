#!/usr/bin/python3

from pymongo import MongoClient
import json

client = MongoClient()
db = client.sw_db
result = db.places.find({'geometry':
                            {'$geoWithin':
                                {'$geometry':
                                    {
                                        "type": "Polygon",
                                        "coordinates": [json.loads(open("polygon.json", "r").read())]
                                    }
                                }
                            }
                        }).count()

open('correct_answer', 'w').write(str(result))
#client.drop_database('sw_db')