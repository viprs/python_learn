#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import os
import sys

if __name__ == '__main__':
    for item in range(10):
        if item % 2 == 0:
            print "元素: %s 是偶数" % item
        else:
            print "元素: %s 是奇数" % item
