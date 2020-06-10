import datetime
import random
import MySQLdb

host="192.168.0.6"
user="root"
password="password"
dbname="db1"

db = MySQLdb.connect(host, user, password, dbname)

names = ['Ruan', 'Stefan', 'James', 'Peter', 'Silver', 'Frank', 'Michelle', 'Samantha', 'Jennifer']
surnames = ['Smith', 'Jacobs', 'James', 'Phillips', 'Anderson']
countries = ['South Africa', 'Italy', 'Sweden', 'England', 'Somoa', 'New York']
job = ['Doctor', 'Scientist', 'Teacher', 'Police Officer', 'Waiter', 'Banker', 'IT']
os = ['Linux', 'Windows', 'Mac']
car = ['Volkswagen', 'Ford', 'Nissan', 'Toyota', 'BMW', 'Audi', 'Mercedez-Benz', 'Mazda', 'Hyundai']

cur = db.cursor()
cur.execute("DROP TABLE IF EXISTS myusers")
cur.execute("CREATE TABLE myusers(name VARCHAR(50), surname VARCHAR(50), countries VARCHAR(50), job VARCHAR(20), os VARCHAR(20), car VARCHAR(20))")

bunch = []
for x in range(100000):
    a = random.choice(names)
    b = random.choice(surnames)
    c = random.choice(countries)
    d = random.choice(job)
    e = random.choice(os)
    f = random.choice(car)

    bunch.append((a, b, c, d, e, f))

# https://mysqlclient.readthedocs.io/user_guide.html
cur.executemany(
    """INSERT INTO myusers(name, surname, countries, job, os, car) VALUES(%s, %s, %s, %s, %s, %s)""",
    bunch
)

db.commit()
db.close()
