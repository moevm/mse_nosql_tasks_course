#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import numpy as np
import json
import random

client = MongoClient()
db = client.sw_db
db.places.create_index([('geometry', GEOSPHERE)])
lasers = np.array(json.load(open('lasers.json', 'r')))
indicies = random.sample(range(103), 75)
db.places.insert_many(lasers[indicies].tolist())
