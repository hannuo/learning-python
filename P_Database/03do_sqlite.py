# -*- coding: utf-8 -*-

import os, sqlite3

#os.path.dirname(__file__)返回脚本的路径
#join：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#os.path.join()：  将多个路径组合后返回
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select * from user where score > ? and score < ?',(low,high))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()
    
# 测试:
#assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
#assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
#assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
get_score_in(80,96)

print('Pass')
