#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Samren'
import random


def guess_magic_num():
    magic = random.randint(0, 9)
    while True:
        print "input 0-9 number:"
        user_input = raw_input()
        if user_input == "q" or user_input == "quit":
            break
        if int(user_input) == magic:
            print "yes, you just guess it right!"
            break


if __name__ == '__main__':
    guess_magic_num()
