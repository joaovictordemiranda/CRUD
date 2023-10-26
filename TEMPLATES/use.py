from test_ import db_insert, db_delete, db_update, db_select
from pprint import pprint


#db_insert('mario', '8080-9090', 'xxmarioggmail.com', '52')
#db_insert('vitoria', '8080-9090', 'alfredo@gmail.com', '29')
#db_insert('damylle','8080-9090', 'damylle@gmail.com', '29')
#db_update('email''mariaalice77@gmail.com', 'id''4')

pprint(db_select('5', 'id'))