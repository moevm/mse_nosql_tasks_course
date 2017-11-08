from pymongo import MongoClient, GEOSPHERE
import json
from statistics import mean

client = MongoClient()
db = client.sw_db

result = list(db.places.find({'geometry':
                                {'$geoWithin':
                                    {'$geometry' : json.loads(open("polygon.json", "r").read())}
                                }
                            }
                     ))


x = mean([mean([item.get('geometry').get('coordinates')[0][0], item.get('geometry').get('coordinates')[1][0]]) for item in result])
y = mean([mean([item.get('geometry').get('coordinates')[0][1], item.get('geometry').get('coordinates')[1][1]]) for item in result])

open('correct_answer', 'w').write(' '.join(list(map(lambda x: str(round(x, 6)), [x, y, len(result)/len(list(db.places.find()))]))))