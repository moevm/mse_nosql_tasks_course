#!/usr/bin/python3

from pymongo import MongoClient, GEOSPHERE
import json
import random

client = MongoClient()
db = client.sw_db

#delete all from DB
client.drop_database('sw_db')
db.places.create_index([('geometry', GEOSPHERE)])

ans = {"type": "Feature",	# create a polygon that is an answer
      "properties": {},
      "geometry": 
         {
        "type": "Polygon",
        "coordinates": [
          [		  #this point is inside our polygon:
            [94.658203125,66.73990169639414 ],
            [random.uniform(96,98),random.uniform(66,67)],
            [random.uniform(97,101),random.uniform(65,66)],
            [random.uniform(94,97),random.uniform(65,66)],
            [94.658203125,66.73990169639414]
          ]
        ]
   }
}
db.places.insert_one(ans)

#put an answer to correct_answer
result = db.places.find(ans)

#write to file only coords of a result (round to 2 digits)
outfile = open('correct_answer', 'w')
count = True	
for x in result:	
    for i in range(5):		#5 vertices
        outfile.write('[')
        count = True
        for j in range(2):	#2 coords
            rou = x["geometry"]["coordinates"][0][i][j]
            outfile.write(str(round(rou, 2)))
            if count:
                outfile.write(',')
            count = False
        outfile.write(']')

outfile.close()


for i in range(10):
    beginX = random.uniform(62, 74)	#first and last point
    beginY = random.uniform(61, 66)	
    doc =  {"type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [beginX, beginY],
            [random.uniform(75, 86),random.uniform(61, 66)],
            [random.uniform(75, 85),random.uniform(54, 61)],
            [random.uniform(63, 74),random.uniform(54, 61)],
            [beginX, beginY]
          ]
        ]
      }
    }
    db.places.insert_one(doc)
