#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib  
import urllib2  
import cookielib
import json  

#登录的主页面  
hosturl = 'http://sww.hi.wkey.cn/web/user/login.html'
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
posturl = 'http://sww.hi.wkey.cn/api/user/regedit.html' 
  
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
#h = urllib2.urlopen(hosturl)  
  
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',  
           'Referer' : 'http://sww.hi.wkey.cn/web/user/login.html',
           'X-Requested-With':'XMLHttpRequest'}  

values ={"nickName":"b","email":"c@knet.cn","passwd":"abc123"}

jdata = json.dumps(values)
#构造Post数据，他也是从抓大的包里分析得出的。  
postData = {
            'dataContent' : jdata
            }  
  
#需要给Post数据编码  
postData = urllib.urlencode(postData)  

#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
print request  
response = urllib2.urlopen(request)  
text = response.read()  
print text


