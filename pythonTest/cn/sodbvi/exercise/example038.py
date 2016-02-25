#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: sodbvi
'''

if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print sum