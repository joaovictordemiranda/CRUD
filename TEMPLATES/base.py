import sqlite3

con = sqlite3.connect('sqlite.db')

cur = con.cursor()

sql = """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
                idade INT NOT NULL,)"""


con.commit()
con.close()