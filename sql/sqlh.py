# UPDATE and DELETE statements

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE population SET population = 7000000 WHERE \
        city='Nairobi City'")

    # delete data
    c.execute("DELETE FROM population WHERE city='Homabay'")

    print "\nNEW DATA:\n"

    c.execute("SELECT * FROM population")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[1]
