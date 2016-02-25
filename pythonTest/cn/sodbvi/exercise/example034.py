#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

def hello_world():
    print 'hello world'

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()