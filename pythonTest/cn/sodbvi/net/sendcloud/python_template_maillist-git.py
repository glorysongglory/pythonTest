# coding:utf-8

import requests

url = "http://sendcloud.sohu.com/webapi/mail.send_template.json"

API_USER = 'abc'
API_KEY = 'abc'

params = {
    "api_user": API_USER,  # 使用api_user和api_key进行验证
    "api_key": API_KEY,
    "to": "sitetest@maillist.sendcloud.org",  # 使用地址列表的别称地址
    "from": "",  # 发信人, 用正确邮件地址替代
    "fromname": "",
    "replyto": "",
    "subject": "",
    "template_invoke_name": "siteUpdate",
    "use_maillist": "true",
    "resp_email_id": "true",
}

r = requests.post(url, data=params)

print r.text
