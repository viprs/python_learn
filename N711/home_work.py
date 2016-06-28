#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NAT  :
192.168.
172.17.
10.0

Python 编程题

在线编代码：http://c.runoob.com/compile/6

0.编写一个程序，要求输出100个1~20以内的随机数


1.编写一个程序，要求计算出从1到100的和。


2.编写一个程序，输入一个数，判断出是奇数还是偶数。


3.打印出斐波那契数列，如：1 1 2 3 5 8 13 ...


4.格式化输出当前时间，如"2016-06-18 11:40:20"


5.构造一个list，包含10个元素，其中元素至少要有3种以上不同类型
如：list_test = [3, "string", (3, 6), ["aa", "bb"], {"x":3, "y":5}, ......]


6.删除上一个list的第3个元素



7.字典操作
{
  "last_seen": "Mon, 09 May 2016 15:48:57 GMT",
  "member_since": "Fri, 29 Apr 2016 00:00:00 GMT",
  "post_count": 0,
  "posts": "http://localhost:5000/api/v1.0/users/10/posts/",
  "url": "http://localhost:5000/api/v1.0/posts/10",
  "username": "sandra87"
}

遍历上面dict的所有key值


遍历上面dict的所有value值


8.简述面向过程开发和面向对象开发的区别
面向过程：编程者指定步骤，缺点：必须知道前人是如何处理数据，如何定义的方法，C不支持面向对象

面向对象：把数据和方整合成为一个对象，更适合开发者模块化工作，C++、Python、Java

9.简述Python中 list 和 tuple 的区别
list：可变容器
tuple：不可变
list[0]
tuple[2]

10.定义一个函数，接受4个字符串参数，其中有一个有默认值，做字符串连接。


11.有一个tuple，内容是多个字符串如：
("apple", "orange", "bag", "desk", "egg", "chair")，用户输入一个单词，如果在tuple里，就返回处于第几个位置（从0开始），如果没有，就返回-1

"""


import random

def get_random_list():
    """
    # 0.编写一个程序，要求输出100个1~20以内的随机数
    :return:
    """
    result = []
    for i in range(100):
        result.append(random.randint(1, 20))
    return result

def get_fib_list(n):
    """
    打印出斐波那契数列，如：[1, 1, 2, 3, 5, 8, 13,] x
    :return:
    """
    fib_list = []
    if n < 1:
        print "error"
    if n == 1:
        fib_list.append(1)
        return fib_list
    if n == 2:
        fib_list.extend([1, 1])
        return fib_list
    if n > 2:
        fib_list = [1, 1]
        for i in range(n-2):
            fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list



def get_current_time():
    """
    格式化输出当前时间，如 "2016-06-18 11:40:20"
    logging
    :return:
    """
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def list_manipulation():
    """
    如：list_test = [3, "string", (3, 6), ["aa", "bb"], {"x": 3, "y": 5}, ......]
    :return:
    """
    list_test = [3, "string", (3, 6),
                 ["aa", "bb"], {"x":3, "y":5},
                 None, True, False, "lin yingfang", "liu lu"]
    print list_test
    del list_test[2]
    print list_test


def dict_manipulation():
    # 7.字典操作

    dict_test = {
        "last_seen": "Mon, 09 May 2016 15:48:57 GMT",
        "member_since": "Fri, 29 Apr 2016 00:00:00 GMT",
        "post_count": 0,
        "posts": "http://localhost:5000/api/v1.0/users/10/posts/",
        "url": "http://localhost:5000/api/v1.0/posts/10",
        "username": "sandra87"
    }
    print dict_test.keys()
    print dict_test.values()

def test_def(str1, str2, str3, str4="byebye"):
    return str1 + str2 + str3 + str4

def test_tuple():
    """
    ("apple", "orange", "bag", "desk", "egg", "chair")，
    用户输入一个单词，如果在tuple里，就返回处于第几个位置（从0开始），
    如果没有，就返回 - 1
    :return:
    """
    tuple1 = ("apple", "orange", "bag", "desk", "egg", "chair")
    while True:
        user_input = raw_input("please input string:")
        for i in range(len(tuple1)):
            if user_input == tuple1[i]:
                print "%s index is %s." % (user_input, i)
                return i
        else:
            print "no, not in tuple1"
            return -1


if __name__ == '__main__':
    #print get_random_list()
    #print get_current_time()
    print get_fib_list(-1)
    print get_fib_list(3)
    print get_fib_list(5)
    list_manipulation()
    dict_manipulation()
    #print test_def("hello ", "world ")
    print test_tuple()