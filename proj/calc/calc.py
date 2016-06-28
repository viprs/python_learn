#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Samren'
import random

def calc():
    print "please input the first number:"
    arg1 = int(raw_input())

    print "please input the operater:"
    op = raw_input()

    print "please input the second number:"
    arg2 = int(raw_input())
    result = None
    if op == '+':
        result = arg1 + arg2
    elif op == '-':
        result = arg1 - arg2
    elif op == '*':
        result = arg1 * arg2
    elif op == '/':
        result = arg1 / arg2
    else:
        print "unsupported operator :("

    if result is not None:
        print result
    else:
        print "there must be something wrong."

if __name__ == '__main__':
    calc()
