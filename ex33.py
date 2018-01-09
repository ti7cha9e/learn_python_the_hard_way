#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/9 13:54
# @Author : wangchao
# @Site : 
# @File : ex33.py
# @Software: PyCharm

i = 0
numbers = []
while i < 6:
    print "At the top i is %d " % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d " % i

print "The numbers: "

for num in numbers:
    print num