#!/usr/bin/python3

from pymongo import MongoClient
import json

client = MongoClient()
db = client.sw_db

result = db.places.find({'loc':
                            {'$geoWithin':
                                {'$geometry' :
                                    {
                                        "type": "Polygon",
                                        "coordinates":
                                            [json.loads(open("polygon.json", "r").read())]
                                    }
                                }
                            }
                        }).count()

open('correct_answer', 'w').write(str(result))
