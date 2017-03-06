# sql.py - Create a SQLite3 table and populate it with data

import sqlite3

# create a new database if teh database doesn't already exist
with sqlite3.connect("blog.db") as connection:

     # get a cursor object used to execute SQL commands
     c = connection.cursor()

     # create the table
     c.execute("""CREATE TABLE posts
              (title TEXT, post TEXT)
               """)


    # insert dummy data into the table
    # Notice how we escaped the apostrophes in the last two INSERT statements.
     c.execute('INSERT INTO posts VALUES("Initial Post", "Welcome to Birika Tuts.")')
     c.execute('INSERT INTO posts VALUES("Lorem Ipsum", "Lorem Ipsum is bae.")')
     c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
     c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
