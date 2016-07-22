#!/usr/bin/env python
# encoding:utf-8

"""交换2个变量的数据"""
x=3
y=4
y, x = x, y
print x,y  #output: 4, 3

"""
尽量使用局部变量
Python检索局部变量比全局变量块，尽量避免global关键字
"""

"""尽量使用in关键字"""
seq = ["apple", "orange", "pairs"]
for item in seq:
    print item

"""
使用延迟加载加速：
    将import 声明移入函数中，仅在需要的时候导入，稍后导入它们

"""
def re_test():
    import re
    re.compile("aa")

"""
为无限循环使用 while 1
while 1 好于 while True
"""

"""
使用列表推导，list comprehension

"""
evens = [i for i in range(10) if i%2 == 0]
print evens
#output: [0, 2, 4, 6, 8]

"""
使用xrange()处理长序列，不要使用range()
原因：xrange在序列中每次调用只产生一个整数元素，
而range()会返回一个完整列表
"""
#好方法
for i in xrange(100):
    print i

#坏方法
for i in range(100):
    print i

"""
使用generator，节省内存和提高性能
"""


"""
使用itertools模块
permutations返回一个列表的全排列
"""
import itertools
iter = itertools.permutations([1,2,3])
print list(iter)

"""
学习bisect模块保持列表排序
bisect.insort()往已排序里面插入元素，
不需要调用sort()来保持容器排序
"""
import bisect
list_num = [1,4,2,7,5]
list_num.sort()
bisect.insort(list_num, 6)
print list_num

"""
Python列表，实际上是一个数组，
    list.insert(0,elem)效率低
    list.append()会更好
deque是一个双向链表
"""


"""
使用dict和set测试成员
它们都是使用哈希表来实现，查找效率可以达到O(1)
"""

mylist = ['a', 'b', 'c'] #不太好，效率低
print 'c' in mylist

myset = set(['a', 'b', 'c']) #更快
print 'c' in myset

"""
理解Python中的GIL（全局解释器锁）
GIL是必要的，因为CPython的内存管理是非线程安全的。
你不能简单地创建多个线程，并希望Python能在多核心的
机器上运行得更快。这是因为 GIL將会防止多个原生线程
同时执行Python字节码。换句话说，GIL將序列化您的所有
线程。然而，您可以使用线程管理多个派生进程加速程序，
这些程序独立的运行于你的Python代码外
"""

"""
像熟悉文档一样的熟悉Python源代码：
Python有些模块为了性能使用C实现。当性能至关重要而
官方文档不足时，可以自由探索源代码。你可以找到底层的
数据结构和算法。 Python的源码库就是一个很棒的地方：
http://svn.python.org/view/python/trunk/Modules
"""

