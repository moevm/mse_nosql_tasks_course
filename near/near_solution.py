from pymongo import MongoClient, GEOSPHERE

client = MongoClient()
db = client.nr

mean = [55.75410148414108, 37.62049198150635]

result = list(db.places.find({'loc':
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
}))

open('correct_answer', 'w').write(str((len(result) / len(list(db.places.find())))))
client.drop_database('nr')