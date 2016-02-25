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

print cursor.rowcount

cursor.close()
conn.close()


print MySQLdb