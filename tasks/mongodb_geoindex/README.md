﻿Задание:
Подключитесь к базе данных "my_db", и в коллекции "places" создайте индекс типа 2dsphere по полю location.

Описание работы:
В скрипте инициализации создается БД my_db, в ней - коллекция places, в эту коллекцию добавляется один документ.
Скрипт проверки получает информацию об индексах в данной коллекции, и если по ключу location_2dsphere имеются данные, значит индекс создан, задача решена.