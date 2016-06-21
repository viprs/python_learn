#!/usr/bin/env python
# -*- coding: utf-8 -*-



d = {'a' : 'apple', 'b' : 'ball', 'c' : 'cat'}
for k in d:
    print k

for k in d.keys():
    if k.startswith('a'):
        del d[k]

#=======================分割线====================
"""
在循环中区分多个出口
"""
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            return i
    if not found:
        return -1
# 下面这种方式更好
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            return i
    else:
        return -1

#=======================分割线====================