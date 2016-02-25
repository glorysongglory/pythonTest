#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

import time

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 暂停一秒
time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))