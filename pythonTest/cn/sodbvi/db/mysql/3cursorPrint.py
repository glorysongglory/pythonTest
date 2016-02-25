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

sql="select * from user"

cursor.execute(sql)

rs=cursor.fetchall()

for row in rs:
    print "userId=%s,userName=%s" % row

cursor.close()
conn.close()


print MySQLdb