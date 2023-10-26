import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('sqlite.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def db_insert(name, phone, email, idade):
    return """
        INSERT  INTO users(name, phone, email, idade)
        VALUES('{}', '{}', '{}', '{}')
        """.format(name, phone, email, idade)

@commit_close
def db_update(email, id):
    return """
    UPDATE users SET email = '{}' WHERE id = '{}'
    """.format(email, id)

@commit_close
def db_delete(id):
    return """
    DELETE FROM users WHERE id='{}'
    """.format(id)

def db_select(data, field):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    sql = """SELECT name, phone, email, idade
    FROM users
    WHERE {}={}""".format(field, data)

    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data