#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print '%d 大于 %d' % (i,j)
    elif i == j:
        print '%d 等于 %d' % (i,j)
    elif i < j:
        print '%d 小于 %d' % (i,j)
    else:
        print '未知'