#!/usr/bin/python3
# -*- coding: utf-8 -*-


from pymongo import MongoClient, GEOSPHERE

def test_index(s):  #what is s?
	client = MongoClient()
	db = client.my_db

	#get information about indexes in db
	a = db.places.index_information()
	str_a = str(a.get("location_2dsphere"))
	assert str_a != "None", "Ваш ответ не совпадает с правильным"

#if (str(a.get("location_2dsphere")) != "None"):   #i.e. index has been created
#	print("correct")
#else:
#	print("incorrect")
