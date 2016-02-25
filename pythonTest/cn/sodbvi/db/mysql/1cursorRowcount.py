import MySQLdb
conn=MySQLdb.Connect(
                     host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='',
                     db='imooc',
                     charset='utf8'
                     )
cursor=conn.cursor()

print cursor
print conn

sql="select * from user"

cursor.execute(sql)

rs=cursor.fetchone()

print rs

rs=cursor.fetchmany(3)

print rs

rs=cursor.fetchall()

print rs

print cursor.rowcount

cursor.close()
conn.close()

