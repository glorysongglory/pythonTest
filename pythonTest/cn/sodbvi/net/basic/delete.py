# -*- coding: UTF-8 -*-
'''
Created on 2016年1月26日

@author: sodbvi
'''

import urllib2
import json

def http_delete():
    url='http://www.baidu.com'
    values={'user':'Smith'}

    jdata = json.dumps(values)
    request = urllib2.Request(url, jdata)
    request.add_header('Content-Type', 'your/conntenttype')
    request.get_method = lambda:'DELETE'        # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_delete()
print resp