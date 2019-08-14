# -*- coding: UTF-8 -*-
'''
Created on 2016年2月22日

@author: sodbvi
'''
from email.mime.text import MIMEText
import time
import smtplib
import cx_Oracle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# ==========================================
# 要发给谁
# ==========================================
mailto_list = ["317878410@qq.com"]
# ==========================================
# 设置服务器，用户名、口令以及邮箱的后缀 
# ==========================================
mail_host = "smtp.test.cn"
mail_user = "test@test.cn"
mail_pass = "123123"
mail_postfix = "12323.com"


# ==========================================
# 发送邮件 
# ==========================================
def send_mail(to_list, sub, nickName):
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("123@qq.com","sub","content")
    '''
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    tmpcontent = """\
  aaaa
  """
    msg = MIMEText(tmpcontent.replace("#NICKNAME#", nickName), 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    db_conn = cx_Oracle.connect("fff/offfem@192.168.100.55/ora9")
curs = db_conn.cursor()
sql = '''select * from ai_user_edm0422 a where  a.id> 451 order by id asc '''
rr = curs.execute(sql)
row = curs.fetchone()
while row:
    (ID,MAIL, NICKNAME) = (row[0],row[8], row[6])
    mailto_list = [MAIL]
    if send_mail(mailto_list, "tewet", NICKNAME.decode('gbk')):
        print str(ID) + " send success"
    else:
        print str(ID) + " send fail"
    row = curs.fetchone()
    time.sleep(1)

