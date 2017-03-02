# QUESTION:
# Create a newdatabase called "cars", and add a table called "inventory"
# that includes the following fields: "Make", "Model", and "Quantity".
# Don't forget to include the proper data-types.

# import sqlite2 library
import sqlite3

# Create/ Estabish connection with db
conn = sqlite3.connect("nganya.db")

# Cursor objesct to execute sql commands
cursor = conn.cursor()

# Create a table
cursor.execute(""" CREATE TABLE cars
                        (Make TEXT, Model TEXT, Quantity INT)
                        """)
# close connection
conn.close
