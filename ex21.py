#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 15:24
# @Author : wangchao
# @Site : 
# @File : ex21.py
# @Software: PyCharm

def add(a,b):
    print "Adding %d + %d: " % (a, b)
    return  a + b

def subtract(a, b):
    print "Subtracting %d - %d: " %(a, b)
    return  a - b

def multiply(a, b):
    print "Multiplying %d * %d: " % (a, b)
    return  a * b

def devide(a, b):
    print "Deviding %d / %d: " % (a, b)
    return  a / b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, devide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand"