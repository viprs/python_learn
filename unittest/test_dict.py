#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'


if __name__ == '__main__':
    print "hello"
    test_dict = {
        "name": "ss",
        "age": 18,
        "location": "shen zhen"
    }
    for key in test_dict:
        print "key: ", key
    print "========我是可爱的分割线=============="
    for (key, value) in test_dict.items():
        print "key: ", key, "value: ", value