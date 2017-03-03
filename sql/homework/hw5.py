# Create a table and populate it with data

"""Add another table to accompany your "inventory" table called "orders".
This table should have the following fields: "make", "model", and "order_date".
Make sure to only include makes and models for the cars found in the inventory table.
Add 15 records (3 for each car), each with a separate order date (YYYY-MM-DD)."""

import sqlite3

with sqlite3.connect("nganya.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders
              (make TEXT, model TEXT, order_date DATE)
               """)

    orders = [
            ('Ford', 'Focus', '2017-03-03'),
            ('Ford', 'Focus', '2017-03-04'),
            ('Ford', 'Focus', '2017-03-05'),
            ('Honda', 'Civic', '2017-03-06'),
            ('Honda', 'Civic', '2017-03-07'),
            ('Honda', 'Civic', '2017-03-08'),
            ('Ford', 'Mustang', '2017-03-09'),
            ('Ford', 'Mustang', '2017-03-10'),
            ('Ford', 'Mustang', '2017-03-11'),
            ('Honda', 'Accord', '2017-03-12'),
            ('Honda', 'Accord', '2017-03-13'),
            ('Honda', 'Accord', '2017-03-14'),
            ('Ford', 'Fiesta', '2017-03-15'),
            ('Ford', 'Fiesta', '2017-03-16'),
            ('Ford', 'Fiesta', '2017-03-17')
            ]

    c.executemany("INSERT into orders VALUES(?, ?, ?)", orders)
    c.execute("SELECT * from orders ORDER BY order_date ASC")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
