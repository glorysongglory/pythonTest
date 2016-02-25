#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print '如果输入的数字小于 50，程序将停止运行。'
again = 1
while again:
    num = int(raw_input('Please input number'))
    print '运算结果为 %d' % (SQ(num))
    if num >= 50:
        again = TRUE
    else:
        again = FALSE