# UPDATE statement

# Update the quantity on two of the records, and then output all of the records
# from the table.

import sqlite3

with sqlite3.connect("nganya.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE cars SET Quantity = 32 WHERE \
        Model = 'Mustang'")

    # update data
    c.execute("UPDATE cars SET Quantity = 26 WHERE \
        Model = 'Fiesta'")

    print "\nNEW DATA:\n"

    c.execute("SELECT * FROM cars")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
