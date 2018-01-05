#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 13:03
# @Author : wangchao
# @Site : 
# @File : ex16.py
# @Software: PyCharm

from sys import argv

script, filename = argv

print "We are going to erase %r. " % filename
print "If you don't want that, hit Ctrl-C(^C). "
print "If you do want taht, press RETURN."

raw_input("?")
print "Open this file..."
target = open(filename, 'w')
print "Truncating the file. GoodBye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

f = open(filename)
print f.read()
f.close()