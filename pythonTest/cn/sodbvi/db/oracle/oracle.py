# -*- coding: UTF-8 -*-
'''
Created on 2016年2月22日

@author: sodbvi
'''
import cx_Oracle
import os


db_conn = cx_Oracle.connect("oem/oem@192.168.100.250/ora9")
curs=db_conn.cursor ()
sql='''select * from ai_user_edm0422 a where a.create_date < to_date('2015-06-01','yyyy-mm-dd')'''
rr=curs.execute (sql)
row=curs.fetchone()
while row:
    (ID,NAME)=(row[8],row[6])
    row=curs.fetchone ()
    print ID,NAME.decode('gbk')