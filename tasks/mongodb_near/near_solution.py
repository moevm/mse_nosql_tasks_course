#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE

client = MongoClient()
db = client.nr

mean = [55.75410148414108, 37.62049198150635]

result = db.places.find({'loc':
    {'$near':
        {'$geometry':
            {
                'type': 'Point',
                'coordinates': mean
            },
            '$minDistance': 10000,
            '$maxDistance': 20000,

        }
    }
}).count()

open('correct_answer', 'w').write(str(result))
#client.drop_database('nr')
