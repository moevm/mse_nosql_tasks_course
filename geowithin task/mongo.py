from pymongo import MongoClient, GEOSPHERE
import json
from statistics import mean

client = MongoClient()
db = client.sw_db
db.places.create_index([('geometry', GEOSPHERE)])

lasers = json.load(open('lasers.json', 'r'))

db.places.insert_many(lasers)

result = list(db.places.find({'geometry':
                                {'$geoWithin':
                                    {'$geometry' : json.loads(open("polygon.json", "r").read())}
                                }
                            }
                     ))

for item in result:
    print(item)
x = mean([mean([item.get('geometry').get('coordinates')[0][0], item.get('geometry').get('coordinates')[1][0]]) for item in result])
y = mean([mean([item.get('geometry').get('coordinates')[0][1], item.get('geometry').get('coordinates')[1][1]]) for item in result])


print(x, y)
print(len(result)/len(list(db.places.find())))

client.drop_database('sw_db')