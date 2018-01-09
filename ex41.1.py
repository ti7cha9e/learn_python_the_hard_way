#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/9 16:42
# @Author : wangchao
# @Site : 
# @File : ex41.1.py
# @Software: PyCharm

class TheThings(object):
    def __init__(self):
        self.number = 0

    def some_function(self):
        print "I got called!"

    def add_me_up(self, more):
        self.number += more
        return self.number

# two different function
a = TheThings()
b = TheThings()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

class TheMultiplier(object):
    def __init__(self, base):
        self.base = base

    def do_it(self, m):
        print m,self.base
        return m * self.base


x = TheMultiplier(a.number)
print x.do_it(b.number)