from pymongo import MongoClient, GEOSPHERE
import json
import random


client = MongoClient()
db = client.sw_db

#удаляем все объекты из БД
client.drop_database('sw_db')
db.places.create_index([('geometry', GEOSPHERE)])


#наш участок. Надо ли его добавлять в бд? - он пересекается сам с собой
'''initial = {"type": "Feature",
      "properties": {},
      "geometry": 
         json.loads(open("test_polygon.json", "r").read())
      
    }
db.places.insert_one(initial)
it = db.places.find(initial)
idd = it[0]["_id"]
print(idd)'''


ans = {"type": "Feature",	#создаем многоугольник, к-й является ответом
      "properties": {},
      "geometry": 
         {
        "type": "Polygon",
        "coordinates": [
          [		  #эта точка лежит внутри нашего участка:
            [94.658203125,66.73990169639414 ],
            [random.uniform(96,98),random.uniform(66,67)],
            [random.uniform(97,101),random.uniform(65,66)],
            [random.uniform(94,97),random.uniform(65,66)],
		#она же:
            [94.658203125,66.73990169639414]
          ]
        ]
   }
}
db.places.insert_one(ans)

#правильный ответ кладем в correct_answer
result = db.places.find(ans)
#записываем в файл только координаты результата (округляя до 2 знаков после , )
#outfile = open('/home/milana/Documents/correct_answer', 'w')
outfile = open('correct_answer', 'w')
count = True	#для красивого вывода 
for x in result:	
    for i in range(5):		#всего 5 вершин
        outfile.write('[')
        count = True
        for j in range(2):	#две координаты
            rou = x["geometry"]["coordinates"][0][i][j]
            outfile.write(str(round(rou, 2)))
            if count:
                outfile.write(', ')
            count = False
        outfile.write('] ')

outfile.close()

#записываем в файл id ответа (для проверки) !!! Как получить первую запись в коллекции?
outfile = open('ans_id', 'w')
for_id = db.places.find(ans)
for x in for_id:
    outfile.write(str(x["_id"]))
outfile.close()


for i in range(10):
    beginX = random.uniform(62, 74)	#первая и последняя точка
    beginY = random.uniform(61, 66)	#чтобы замкнуть фигуру
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
