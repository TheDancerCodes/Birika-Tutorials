# QUESTION:
# Using the "cars" table from the previous homework assignment[hw1.py],
# add (INSERT) 5 records (rows of data) to the table.

# Make sure 3 of the vehicles are Fords while the other 2 are Hondas.
# Use any model and quantity for each.

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("nganya.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT into cars VALUES('Ford', 'Focus', 10)")
cursor.execute("INSERT into cars VALUES('Ford', 'Mustang', 12)")
cursor.execute("INSERT into cars VALUES('Ford', 'Fiesta', 20)")
cursor.execute("INSERT into cars VALUES('Honda', 'Civic', 24)")
cursor.execute("INSERT into cars VALUES('Honda', 'Accord', 22)")

# commit the changes
conn.commit()

# close the database connection
conn.close()
