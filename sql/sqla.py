# Create an SQLite3 database and table

# import sqlite3 library
import sqlite3

# create a new dtabase if the database doesn't already exist.
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

# close the database connection
conn.close()
