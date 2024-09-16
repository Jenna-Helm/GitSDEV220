# 16.4
import sqlite3


# Connect to the SQLite database
conn = sqlite3.connect('books.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

conn.commit()
conn.close()

# 16.6
import sqlite3

# Connect
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Alphabetical order code
cursor.execute('SELECT title FROM books ORDER BY title ASC')
titles = cursor.fetchall()
for title in titles:
    print(title[0])

conn.close()