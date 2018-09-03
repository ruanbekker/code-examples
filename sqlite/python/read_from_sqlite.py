import sqlite3 as sql

product_name = 'guitar'

db_connection = sql.connect('db.sql')
c = db_connection.cursor()

try:
    c.execute('select product_description from products where product_name = "{k}"'.format(k=product_name))
    data = c.fetchone()[0]
    db_connection.close()
    print("=> Product: {p}, Description: {d}".format(p=product_name, d=data))
except:
    print('issue occured')

# to create the data:
# $ sqlite3 db.sql -header -column
# import sqlite3 as sql
# SQLite version 3.16.0 2016-11-04 19:09:39
# Enter ".help" for usage hints.
# 
# sqlite> create table products (product_name STRING(32), product_description STRING(32));
# sqlite> insert into products values('apple', 'fruit called apple');
# sqlite> insert into products values('guitar', 'musical instrument');
# sqlite> select * from products;
# product_name  product_description
# ------------  -------------------
# apple         fruit called apple
# guitar        musical instrument
# sqlite> .exit
