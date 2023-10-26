from test_ import db_insert, db_delete, db_update, db_select
from pprint import pprint


db_insert('fabio', '8080-9090', 'xxxxfabio52@gmail.com','52')
db_insert('maria vitoria', '8080-9090', 'axxxkogu@gmail.com', '22')
db_insert('maria damylle','(21)8080-9090', 'damyllekogu@gmail.com', '25')
#pprint(db_select('joao', 'name'))