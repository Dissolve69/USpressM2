import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()


cur.execute("create table test (num INTEGER PRIMARY KEY AUTOINCREMENT, publisher TEXT, date TEXT, title TEXT, author TEXT, links TEXT UNIQUE ON CONFLICT IGNORE, contents TEXT)")
conn.commit()

cur.execute("select * from test")
rows = cur.fetchall()
print (rows)

conn.close()
