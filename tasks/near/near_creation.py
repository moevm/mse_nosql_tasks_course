import numpy as np
from pymongo import MongoClient, GEOSPHERE

mean = [55.75410148414108, 37.62049198150635]
cov = [[0.04, 0],[0, 0.04]]
xy = np.random.multivariate_normal(mean, cov, 100000)

client = MongoClient()
db = client.nr
db.places.create_index([('loc', GEOSPHERE)])

justalist = [{'loc': {'type' : 'Point','coordinates' : item.tolist() }} for item in xy]

db.places.insert_many(justalist)