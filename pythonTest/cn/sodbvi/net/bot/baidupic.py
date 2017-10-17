# -*- coding:utf-8 -*-
import os
import re

import requests

url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1508145815585_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1508145815586%5E00_1349X662&word=rng'

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
i = 0
path = 'D:\\pytestdir\\baidu'
if not os.path.exists(path):
    os.makedirs(path)
for each in pic_url:
    print(each)
    try:
        pic = requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        continue

    string = path + '\\' + str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
