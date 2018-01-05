#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/4 17:12
# @Author : wangchao
# @Site : 
# @File : ex6.py
# @Software: PyCharm

x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those %s. " % (binary, do_not)
print x
print y

print "I said: %r. " % x
print "I also said: %r. " % y

hilarious = False
joke_evalution = "Isn't that joke so funny?! %r"
print joke_evalution % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e