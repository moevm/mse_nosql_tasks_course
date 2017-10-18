#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import json

client = MongoClient()
db = client.sw_db

query = {'geometry':
           {'$geoIntersects':
               {'$geometry' : json.loads(open("test_polygon.json", "r").read())}
           }
        }

result = db.places.find(query)

#write to file only coords of a result (round to 2 digits)
outfile = open('correct_answer', 'w')
for x in result:	
    for i in range(5):		#5 vertices
        outfile.write('[')
        count = True
        for j in range(2):	#2 coords
            rou = x["geometry"]["coordinates"][0][i][j]
            outfile.write(str(round(rou, 2)))
            if count:
                outfile.write(', ')
            count = False
        outfile.write('] ')

outfile.close()

client.drop_database('sw_db')