#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 11:18
# @Author : wangchao
# @Site : 
# @File : ex15.py
# @Software: PyCharm

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
print txt.read()

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()

txt.close()
txt_again.close()