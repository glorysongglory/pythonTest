#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

def age(n):
    if n == 1:
         c = 10
    else: 
        c = age(n - 1) + 2
    return c
print age(5)