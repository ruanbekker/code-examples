import sqlite3
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('select count(*) as num, city from people group by city')
rows = cur.fetchall()

for row in rows:
    print("{}, {}".format(row['num'], row['city']))

# output:
# 555346, auckland
# 556127, bloemfontein
# 555049, cape town
# 555350, dublin
# 556027, johannesburg
# 555961, kroonstad
# 555740, port elizabeth
# 555645, pretoria
# 554750, sydney
