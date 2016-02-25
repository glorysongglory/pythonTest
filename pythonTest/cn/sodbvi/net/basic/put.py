# -*- coding: UTF-8 -*-
'''
Created on 2016年1月26日

@author: sodbvi
'''

import urllib2
import json

def http_put():
    url='http://www.baidu.com'
    values={'':''}

    jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
    request = urllib2.Request(url, jdata)
    request.add_header('Content-Type', 'your/conntenttype')
    request.get_method = lambda:'PUT'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_put()
print resp