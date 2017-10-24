#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import json
import random
from math import ceil

client = MongoClient()
db = client.sw_db
db.places.create_index([('loc', GEOSPHERE)])
lasers = json.load(open('lasers.json', 'r'))
indicies = random.sample(range(len(lasers)), ceil(len(lasers)*0.75))
db.places.insert_many([lasers[ind] for ind in indicies])
