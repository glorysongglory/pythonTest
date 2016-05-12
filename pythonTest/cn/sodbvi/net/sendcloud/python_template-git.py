#coding:utf-8                                                                   

import requests, json                                                                

url = "http://sendcloud.sohu.com/webapi/mail.send_template.json"                         

API_USER = 'abc'
API_KEY = '123'

sub_vars = {
    'to': ['123@qq.com'],
    'sub': {
        '%nickname%': ['老123,呵呵'],
    }
}

params = {
    "api_user": API_USER, # 使用api_user和api_key进行验证                       
    "api_key" : API_KEY,                                             
    "template_invoke_name" : "abc",
    "substitution_vars" : json.dumps(sub_vars),
    "from" : "abc@123.com", # 发信人, 用正确邮件地址替代
    "replyto" : "abc@123.com",
    "fromname" : "123",
    "subject" : "123",
    "resp_email_id": "true",
}

r = requests.post(url,  data=params)

print r.text

