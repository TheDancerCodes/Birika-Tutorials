# Create a table and populate it with data

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE counties
                (city TEXT, region TEXT)
                """)

    # insert multiple records using a tuple
    cities = [
                ('Nairobi City', 'Nairobi'),
                ('Nakuru', 'RiftValley'),
                ('Naivasha', 'RiftValley'),
                ('Narok', 'RiftValley'),
                ('Mombasa', 'Coast'),
                ('Mandera', 'NorthEastern'),
                ('Kakamega', 'Western'),
                ('Kajiado', 'RiftValley'),
                ('Kisumu', 'Nyanza'),
                ('Kiambu', 'Central'),
                ('Machakos', 'Eastern'),
                ('Trans Nzoia', 'RiftValley'),
                ('Meru', 'Eastern'),
                ('Baringo', 'RiftValley'),
                ('Bungoma', 'Western')
    ]

    c.executemany("INSERT INTO counties VALUES(?, ?)", cities)

    c.execute("SELECT * from counties ORDER BY region ASC")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
