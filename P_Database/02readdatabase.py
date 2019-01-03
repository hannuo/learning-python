import sqlite3

conn = sqlite3.connect('hanhan.db')

cursor = conn.cursor()

cursor.execute('select * from user where id=?',('1',))

values = cursor.fetchall()

print(values)

cursor.execute('select * from user where id=? and name=?',('2','hanhan2'))

values = cursor.fetchall()

print(values)


cursor.close()

conn.close()
