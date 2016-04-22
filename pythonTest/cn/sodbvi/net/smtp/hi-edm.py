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
  <!doctype html><html><head><meta charset="utf-8"><title>letter</title><style>body,div,h1,p,a,em,span,ul,li{margin:0;padding:0}body{font-family:'微软雅黑'}a{text-decoration:none}li{list-style:none}div.page{width:980px;height:800px;background:#eeeff1;margin:0 auto}h1.title{width:100%;height:105px;text-align:center;line-height:105px}h1.title span{color:#569bff}.content{width:700px;height:532px;background:#fff;margin-left:140px}.top{width:100%;height:342px;border-bottom:1px solid#efefef;padding-top:48px;font-size:16px}.top p.dear{margin-left:242px;height:16px;font-size:16px;font-style:italic}.top ul{width:180px;height:100px;margin-left:270px;color:#666;font-style:italic}.top ul li{margin-top:12px}.top div.des{margin-top:35px;margin-left:170px;color:#333}.top div.des p{margin-top:12px}.top a.tour{display:block;width:240px;height:56px;border-radius:25px;color:#fff;background:#579bfe;margin-top:28px;margin-left:230px;line-height:56px;text-align:center}.down ul{margin-top:26px;font-size:12px;color:#999}.down li{margin-bottom:11px;text-align:center}.down a{color:#2cb8f6}</style></head><body><div class="page"><h1 class="title"><span>Hi</span>现场</h1><div class="content"><div class="top"><p class="dear"><strong>亲爱的<span>#NICKNAME#</span>:</strong></p><ul><li>原谅我很久未与你来信，</li><li>但我未有一刻把你忘记。</li><li>迟来的问候，</li><li>只为把更好的展现给你。</li></ul><div class="des"><p>此刻起，全新的容貌、新颖的功能、独特的玩法，</p><p>用我的真诚，邀你一同踏上【Hi现场】互动之旅。</p></div><a class="tour"href="http://www.hixianchang.com">开启Hi现场互动之旅</a></div><div class="down"><ul><li><a href="http://www.hixianchang.com">「Hi现场」</a>免费、简单、好用的，现场互动大屏幕制作工具。</li><li>如果你在使用过程中遇到任何问题，欢迎及时向我们反馈。</li><li>有你的支持，相信未来更美好。</li><li>Hi现场团队<a href="http://www.hixianchang.com">hi@hixianchang.com</a></li></ul></div></div></div></body></html>
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
