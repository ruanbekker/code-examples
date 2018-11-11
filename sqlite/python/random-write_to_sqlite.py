import sqlite3, random

names = ['ruan', 'stefan', 'philip', 'norman', 'frank', 'pete', 'johnny', 'peter', 'adam']
cities = ['cape town', 'johannesburg', 'pretoria', 'dublin', 'kroonstad', 'bloemfontein', 'port elizabeth', 'auckland', 'sydney']
lastnames = ['smith', 'bekker', 'admams', 'phillips', 'james', 'adamson']
words = ['some really random text', 'this is more random text with stupid words', 'this is a hello world string', 'this is going to be fun - bhla blah blah blah blah bhla blah blah blah blahbhla blah blah blah blahbhla blah blah blah blahbhla blah blah blah blahbhla blah blah blah blahbhla blah blah blah blah']

conn = sqlite3.connect('database-large.db')
conn.execute('CREATE TABLE IF NOT EXISTS people (name STRING, age INTEGER, surname STRING, city STRING, favorite_words STRING)')

conn = sqlite3.connect('database-large.db')
for x in range(1,1000000):
    conn.execute('INSERT INTO people VALUES("{}", "{}", "{}", "{}", "{}")'.format(random.choice(names), random.randint(18,40), random.choice(lastnames), random.choice(cities), random.choice(words)))
    conn.execute('INSERT INTO people VALUES("{}", "{}", "{}", "{}", "{}")'.format(random.choice(names), random.randint(18,40), random.choice(lastnames), random.choice(cities), random.choice(words)))
    conn.execute('INSERT INTO people VALUES("{}", "{}", "{}", "{}", "{}")'.format(random.choice(names), random.randint(18,40), random.choice(lastnames), random.choice(cities), random.choice(words)))
    conn.execute('INSERT INTO people VALUES("{}", "{}", "{}", "{}", "{}")'.format(random.choice(names), random.randint(18,40), random.choice(lastnames), random.choice(cities), random.choice(words)))
    conn.execute('INSERT INTO people VALUES("{}", "{}", "{}", "{}", "{}")'.format(random.choice(names), random.randint(18,40), random.choice(lastnames), random.choice(cities), random.choice(words)))

conn.commit()
conn.close()
