#!/usr/bin/env python
# encoding:utf-8

"""
因为GIL会序列化线程，导致Python中的多线程
不能再多核机器和集群中加速。
multiprocessing模块，通过派生额外的进程代替
线程，绕过GIL限制，

注意：进程开销比线程开销昂贵，因为线程自动共享
内存地址空间和文件描述符，意味着，创建进程比
创建线程会花费更多，也可能花费更多内存，这点要
牢记！
"""
from ctypes import cdll, CDLL
cdll.LoadLibrary("libc.so.6")
libc = CDLL("libc.so.6")
for i in range(10):
    print libc.random() % 10