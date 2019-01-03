import mysql.connector

# mysql1.py
config = {
    'host': '116.62.61.95',
    'user': 'root',
    'password': 'password2018',
    'port': 3306,
    'database': 't1',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    sql_query = 'select name from user ;'
    cursor.execute(sql_query)
    for name in cursor:
        print (name)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()
