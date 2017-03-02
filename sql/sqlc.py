# executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [
            ('Nakuru', 'NAX', 600000),
            ('Naivasha', 'NVS', 270000),
            ('Narok', 'NRK', 146000),
            ('Homabay', 'HBY', 340000)
             ]

    # insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

# NOTE:
# Parametrized statements(?) should always be used when communicating with a SQL
# database due to potential SQL injections that could occur from using string substitutions(%s).
