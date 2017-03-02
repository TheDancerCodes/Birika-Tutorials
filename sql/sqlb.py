# INSERT Command

# import the sqlite3 Command
import sqlite3

# create the connection object
with sqlite3.connect("new.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    c.execute("INSERT INTO population VALUES('Nairobi City', \
        'NBO', 4200000)")

    c.execute("INSERT INTO population VALUES('Eldoret City', \
        'ELD', 2500000)")
