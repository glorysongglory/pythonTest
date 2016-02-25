# -*- coding: UTF-8 -*-
'''
Created on 2016年1月26日

@author: sodbvi
'''
import urllib2

def http_get():
    url='http://www.baidu.com'   #页面的地址
    response = urllib2.urlopen(url)         #调用urllib2向服务器发送get请求
    return response.read()                     #获取服务器返回的页面信息
    
ret = http_get()
print("RET %r" % (ret))