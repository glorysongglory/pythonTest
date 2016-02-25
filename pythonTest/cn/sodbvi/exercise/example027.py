#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

def output(s,l):
    if l==0:
       return
    print (s[l-1])
    output(s,l-1)
 
s = raw_input('Input a string:')
l = len(s)
output(s,l)