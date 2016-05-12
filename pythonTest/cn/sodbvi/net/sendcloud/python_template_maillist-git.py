# coding:utf-8

import requests

url = "http://sendcloud.sohu.com/webapi/mail.send_template.json"

API_USER = 'abc'
API_KEY = '123'

params = {
    "api_user": API_USER,  # 使用api_user和api_key进行验证
    "api_key": API_KEY,
    "to": "123@abc.org",  # 使用地址列表的别称地址
    "from": "abc@123.com",  # 发信人, 用正确邮件地址替代
    "fromname": "123",
    "replyto": "abc",
    "subject": "123",
    "template_invoke_name": "sadf",
    "use_maillist": "true",
    "resp_email_id": "true",
}

r = requests.post(url, data=params)

print r.text
