import datetime
import random
import MySQLdb
import time

db = MySQLdb.connect('192.168.1.1', 'root', 'password', 'test-db')

con = db.cursor()
con.execute("SELECT * from myusers")

rows = con.fetchall()

for row in rows:
    a_name = row[0]
    a_surnames = row[1]
    a_country = row[2]
    a_gender = row[3]
    a_os = row[4]
    a_car = row[5]

    print a_name, a_surnames, a_country, a_gender, a_os, a_car
