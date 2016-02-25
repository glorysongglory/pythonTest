#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年2月19日

@author: sodbvi
'''
#-*-coding:utf-8-*-  
#========================================== 
# 导入smtplib和MIMEText 
#========================================== 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('d:\\google.py', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.py"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#构造附件2
att2 = MIMEText(open('d:\\emojis.js', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="test1.js"'
msg.attach(att2)

#加邮件头
msg['to'] = '317878410@qq.com'
msg['from'] = '317878410@qq.com'
msg['subject'] = 'hello world'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.qq.com')
    server.login('317878410','gloryliu198710')#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print '发送成功'
except Exception, e:  
    print str(e) 