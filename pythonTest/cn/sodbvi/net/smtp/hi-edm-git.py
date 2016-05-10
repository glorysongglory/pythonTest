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
  <!doctype html><html><head><meta charset="utf-8"><title>letter</title><style>body,div,h1,p,a,em,span{margin:0;padding:0}body{font-family:'微软雅黑'}</style></head><body><div style="width:980px;height:800px;background:#eeeff1;margin:0 auto"><h1 style="width:100%;height:105px;text-align:center;line-height:105px"><span style="color:#569bff">Hi</span>现场</h1><div style="width:700px;height:532px;background:#fff;margin-left:140px"><div style="width:100%;height:350px;border-bottom:1px solid #efefef;padding-top:48px;font-size:16px"><p style="margin-left:242px;height:16px;font-size:16px;font-style:italic"><strong>亲爱的<span>#NICKNAME#</span>:</strong></p><ul style="margin:0;padding:0;margin-left:270px;width:100%;color:#666;font-style:italic;margin-top:12px;font-size:16px"><li style="list-style:none">原谅我很久未与你来信，</li><li style="list-style:none;margin-top:12px">但我未有一刻把你忘记。</li><li style="list-style:none;margin-top:12px">迟来的问候，</li><li style="list-style:none;margin-top:12px">只为把更好的展现给你。</li></ul><div style="margin-top:42px;margin-left:170px;color:#333"><p>此刻起，全新的容貌、新颖的功能、独特的玩法，</p><p style="margin-top:12px">用我的真诚，邀你一同踏上【Hi现场】互动之旅。</p></div><a style="text-decoration:none;display:block;width:240px;height:56px;border-radius:25px;color:#fff;background:#579bfe;margin-top:26px;margin-left:230px;line-height:56px;text-align:center" href="http://www.hixianchang.com">开启Hi现场互动之旅</a></div><div style="width:100%;height:171px"><ul style="margin:0;padding:0;font-size:12px;color:#999;width:100%;height:75px;margin-top:20px"><li style="list-style:none;margin-bottom:8px;text-align:center"><a style="text-decoration:none;color:#2cb8f6" href="http://www.hixianchang.com">「Hi现场」</a> 免费、简单、好用的，现场互动大屏幕制作工具。</li><li style="list-style:none;margin-bottom:8px;text-align:center">如果你在使用过程中遇到任何问题，欢迎及时向我们反馈。</li><li style="list-style:none;margin-bottom:8px;text-align:center">有你的支持，相信未来更美好。</li><li style="list-style:none;margin-bottom:8px;text-align:center">Hi现场团队 <a style="text-decoration:none;color:#2cb8f6" href="http://www.hixianchang.com">hi@hixianchang.com</a></li></ul></div></div></div></body></html>
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

