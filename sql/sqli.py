# executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [
                ('Mombasa', 'MSA', 939370),
                ('Mandera', 'MDR', 1025756),
                ('Kakamega', 'KMG', 1660651),
                ('Kajiado', 'KDO', 687312),
                ('Kisumu', 'KSM', 968909),
                ('Kiambu', 'KBU', 1623282),
                ('Machakos', 'MKS', 1098584),
                ('Trans Nzoia', 'TNZ', 818757),
                ('Meru', 'MRU', 1356301),
                ('Baringo', 'BO', 555561),
                ('Bungoma', 'BG', 1630934)
            ]

    c.executemany("INSERT into population VALUES(?, ?, ?)", cities)

    c.execute("SELECT * from population WHERE population > 1000000")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
