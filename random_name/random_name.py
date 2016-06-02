#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import random


def random_name():
    h_file = open('name_list.txt', 'r')
    name_list = h_file.readlines()
    #method 1
    #random_num = random.randint(0, len(name_list)-1)
    #print random_num, name_list[random_num]

    #method 2
    print random.choice(name_list)


if __name__ == '__main__':
    random_name()