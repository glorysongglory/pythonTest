# -*- coding: UTF-8 -*-
'''
Created on 2016年2月22日

@author: sodbvi
'''
import cx_Oracle
import os


db_conn = cx_Oracle.connect("oem/oem@202.173.9.77/oragbk")
curs=db_conn.cursor ()
sql='select * from ai_wallmoney'
rr=curs.execute (sql)
row=curs.fetchone()
while row:
    (ID,NAME)=(row[5],row[6])
    row=curs.fetchone ()
    print ID,NAME.decode('gbk')