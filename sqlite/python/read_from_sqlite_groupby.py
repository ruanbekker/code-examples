import sqlite3
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('select count(*) as num, city from people group by city')
rows = cur.fetchall()

for row in rows:
    print("{}, {}".format(row['num'], row['city']))

# output:
# 2, cape town
# 1, johannesburg
# 1, kroonstad
