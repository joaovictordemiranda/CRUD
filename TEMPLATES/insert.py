import sqlite3

def db_insert(name, phone, email):
    return """
    INSERT  INTO users(name, phone, email)
        VALUES('{}', '{}', '{}')
    """.format(name, phone, email)

con = sqlite3.connect('sqlite.db')

cur = con.cursor()

cur.execute(db_insert('miguel', '8000-6174', 'miguelCristianoronaldo@gmail.com'))

con.commit()
con.close()

