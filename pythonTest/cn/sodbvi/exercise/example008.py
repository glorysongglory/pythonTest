#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print '%d * %d = % -10d' % (i,j,result)
    print ''