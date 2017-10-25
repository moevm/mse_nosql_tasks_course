Отряд повстанцев перестреливается с имперскими штурмовиками прямо в Центральном парке Нью-Йорка!
Определите какие из лучей находятся внутри многоугольника.

В файле polygon.json даны координаты многоугольника.

Для облегчения работы можно воспользоваться автоматической загрузкой координат многоугольника

В mongo shell выполните команду load("polygon.js") (В load указывается путь до файла. Путь зависит от места запуска mongo shell)

В результате выполнения этой команды в переменной polygon будет храниться [[x1,y1],[x2,y2], ..., [xn, yn]]

Теперь вместо массива координат можно использовать переменную polygon.

В файл ответа 'answer' выведите количество лазерных лучей находящихся внутри многоугольника от всех лучей в коллекции.