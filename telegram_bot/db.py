import sqlite3

conn = sqlite3.connect('tourism.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL UNIQUE)''')

cursor.execute('''CREATE TABLE places
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   city_id INTEGER NOT NULL,
                   FOREIGN KEY(city_id) REFERENCES cities(id))''')

cities = [('Анталия',),
          ('Кемер',),
          ('Аланья',)]

places = [('Пляж Клеопатры', 3),
          ('Замок Аланьи', 3),
          ('Аквапарк The Land of Legends', 1),
          ('Музей Античного Театра Аспендоса', 2)]

cursor.executemany('INSERT INTO cities(name) VALUES (?)', cities)
cursor.executemany('INSERT INTO places(name, city_id) VALUES (?, ?)', places)

conn.commit()