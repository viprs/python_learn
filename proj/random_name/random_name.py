#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Samren'
import random
from random import seed

def random_name():
    h_file = open('name_list.data', 'r')
    name_list = h_file.readlines()
    print name_list
    # method 1
    seed()
    random_num = random.randint(0, len(name_list) - 1)
    lucky_guy = name_list[random_num]
    print lucky_guy

    # method 2
    # print random.choice(name_list)
    h_file.close()
    w_file = open("lucky_guy.data", "w")
    w_file.write(lucky_guy)
    w_file.close()

if __name__ == '__main__':
    random_name()
