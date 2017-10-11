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

#записываем в файл только координаты результата (округляя до 2 знаков после , )
outfile = open('correct_answer', 'w')
for x in result:		
    for i in range(5):		#всего 5 вершин
        outfile.write('[')
        for j in range(2):	#две координаты
            rou = x["geometry"]["coordinates"][0][i][j]
            outfile.write(str(round(rou, 2)))
            outfile.write(', ')
        outfile.write('], ')

outfile.close()

client.drop_database('sw_db')
