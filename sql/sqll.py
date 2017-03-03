# JOINing data from multiple tables - cleanup

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT population.city,
        population.population,
                counties.region FROM population, counties WHERE
                population.city = counties.city ORDER BY
                    population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print
