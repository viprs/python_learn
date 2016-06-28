#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0
while True:
    print "count is:", count
    count += 1

# set操作

empty_set = {}
set_value = {1, 2, 3}

print empty_set
print set_value

set_value.add(2)
print set_value

set_value.add("banana")
print set_value

set_value.remove(3)
print set_value


# dict 操作

dict = {'Alice': '2341',
        'Beth': '9102',
        'Cecil': '3258'}

print "Alice 的学号是:", dict['Alice']
print "Beth 的学号是:", dict['Beth']
print "Cecil 的学号是:", dict['Cecil']

dict["John"] = '0711'
print dict
dict["Alice"] = '999'
print dict

print "keys 是：", dict.keys()

for key in dict.keys():
    print "%s 的学号是: %s" % (key, dict[key])