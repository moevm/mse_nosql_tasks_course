#!/usr/bin/python3

import numpy as np
from pymongo import MongoClient, GEOSPHERE


def addRandomPoints(fromX, toX, fromY, toY, size=50):
    x = np.random.uniform(low=fromX, high=toX, size=size)
    y = np.random.uniform(low=fromY, high=toY, size=size)
    db.places.insert_many([
        {
            'geometry':
                {
                    'type': 'Point',
                    'coordinates': list(item)
                }
        }
    for item in zip(x, y)])

client = MongoClient()
db = client.database
db.places.create_index([('geometry', GEOSPHERE)])

value = np.random.randint(low=15, high=50)
addRandomPoints(-125.42, -115.09, 41.7, 48.02, value)
addRandomPoints(-107.18, -99.62, 37.16, 46.16, value)
addRandomPoints(-114.38, -106.3, 51.37, 55.97, value)
addRandomPoints(-113.33, -109.42, 46.71, 48.8, value)

correct_answer = value * 4

addRandomPoints(0, 10, 0, 10)

open('correct_answer', 'w').write(str(correct_answer))
