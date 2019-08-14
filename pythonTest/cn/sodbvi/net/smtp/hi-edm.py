#-*-coding:utf-8-*-
#========================================== 
# 导入smtplib和MIMEText 
#========================================== 
from email.mime.text import MIMEText 
import smtplib 
#========================================== 
# 要发给谁
#========================================== 
mailto_list=["XX@qq.com"]
#========================================== 
# 设置服务器，用户名、口令以及邮箱的后缀 
#========================================== 
mail_host="smtp.qq.com"
mail_user="XX"
mail_pass="YY"
mail_postfix="qq.com"
#========================================== 
# 发送邮件 
#========================================== 
def send_mail(to_list,sub,nickName):
  ''''' 
  to_list:发给谁 
  sub:主题 
  content:内容 
  send_mail("123@qq.com","sub","content") 
  '''
  me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
  tmpcontent="""\

  """
  msg = MIMEText(tmpcontent.replace("#NICKNAME#",nickName),'html','utf-8')
  msg['Subject'] = sub 
  msg['From'] = me 
  msg['To'] = ";".join(to_list) 
  try: 
    s = smtplib.SMTP() 
    s.connect(mail_host) 
    s.login(mail_user,mail_pass) 
    s.sendmail(me, to_list, msg.as_string()) 
    s.close() 
    return True
  except Exception, e: 
    print str(e) 
    return False
if __name__ == '__main__': 
  if send_mail(mailto_list,"here is subject",'sodbvi'):
    print "发送成功"
  else: 
    print "发送失败"
