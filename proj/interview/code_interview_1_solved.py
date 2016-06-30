#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.编写一个程序，要求计算出从1到100的和。
def sum(value):
    result = 0
    for i in range(1, value+1):
        result += i
        # result = result + i
    return result


# 2.编写一个程序，输入一个数，判断出是奇数还是偶数。
def is_odd_even():
    # a_z A-Z _ 0-9
    print "please input a value:"
    get_value = int(raw_input())

    if get_value % 2 == 1:
        print "%d is odd" % get_value
    else:
        print "%d is even" % get_value


if __name__ == '__main__':
    # print sum(3)
    # print sum(100)
    is_odd_even()