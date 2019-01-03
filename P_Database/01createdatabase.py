import sqlite3

# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('hanhan.db')

cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')

cursor.execute('insert into user (id,name) values (\'1\',\'hanhan\')')

cursor.execute('insert into user (id,name) values (\'2\',\'hanhan2\')')

cursor.execute('insert into user (id,name) values (\'3\',\'hanhan3\')')

print(cursor.rowcount)

cursor.close()

conn.commit()

conn.close()
