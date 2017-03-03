# JOINing data from multiple tables

"""Finally output the car's make and model on one line,
the quantity on another line, and then the order_dates on subsequent lines below that."""

import sqlite3

with sqlite3.connect("nganya.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT cars.make, cars.model,
            cars.quantity, orders.order_date FROM cars INNER JOIN orders
            ON cars.model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3]
        print()
