#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

letter = raw_input("please input:")
#while letter  != 'Y':
if letter == 'S':
    print ('please input second letter:')
    letter = raw_input("please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('data error')
    
elif letter == 'F':
    print ('Friday')
    
elif letter == 'M':
    print ('Monday')
    
elif letter == 'T':
    print ('please input second letter')
    letter = raw_input("please input:")
 
    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('data error')
        
elif letter == 'W':
    print ('Wednesday')
else:
    print ('data error')