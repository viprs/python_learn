#!/usr/bin/env python
# encoding:utf-8


"""
使用方法: 进入cmd.exe
python -m cProfile 4.cprofiles_test.py
"""
import time
def fast():
    time.sleep(0.001)

def slow():
    time.sleep(0.01)

def very_slow():
    for i in xrange(100):
        fast()
        slow()
    time.sleep(0.01)

def main():
    very_slow()
    very_slow()

if __name__ == "__main__":
    main()