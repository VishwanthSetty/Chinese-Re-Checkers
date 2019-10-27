
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

t = ('nikhil',)
c.execute('SELECT * FROM scores WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
data = [('veman',35),
             ('hemanth',20),
             ('ramesh',53),
            ]
c.executemany('INSERT INTO scores VALUES (?,?,?,?,?)', data)




for row in c.execute('SELECT * FROM scores ORDER BY score'):
        print(row)

