
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

t = ('nikhil',)
c.execute('SELECT * FROM scores WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
data = [('hrithik',10),
             ('vishwanth',30),
             ('sriram', 53),
            ]
c.executemany('INSERT INTO scores VALUES (?,?,?,?,?)', data)