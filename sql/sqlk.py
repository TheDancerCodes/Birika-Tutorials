# JOINing data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data: table_name.column_name
    c.execute("""SELECT population.city, population.population,
            counties.region FROM population, counties
            WHERE population.city = counties.city""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
