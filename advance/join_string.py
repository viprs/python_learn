#!/usr/bin/env python
# encoding:utf-8
import os

"""
使用join()连接字符串、拼接路径等
"""

test_list = ["This", "is", "a", "test", "string."]
print " ".join(test_list) #用空格连接list内的每个元素

"""
根据操作系统拼接字符串
os.path.join(参数1, 参数2, 参数3, ...)
"""
print os.path.join("c:\\", "windows", "path")

