#!/usr/bin/python3
# -*- coding: utf-8 -*-


from pymongo import MongoClient, GEOSPHERE

client = MongoClient()
db = client.my_db

#get information about indexes in db
a = db.places.index_information()


if (str(a.get("location_2dsphere")) != "None"):   #i.e. index has been created
	print("correct")
else:
	print("incorrect")
