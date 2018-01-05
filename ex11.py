#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 10:08
# @Author : wangchao
# @Site : 
# @File : ex11.py
# @Software: PyCharm

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
print "So, you're %r old, %r tall, %r heavy." % (age, height, weight)

age = raw_input("How old are you? ")
print "So, you're %r old, %r tall, %r heavy." % (age, height, weight)