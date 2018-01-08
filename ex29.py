#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/8 14:30
# @Author : wangchao
# @Site : 
# @File : ex29.py
# @Software: PyCharm

people = 20
cats = 30
dogs = 15

if people < cats :
    print "Too many cats! The world is doomed!"

if people > cats :
    print "Not many cats! The world is saved!"

if people < dogs :
    print "The world is drooled on!"

if people > dogs :
    print "The world is dry!"

dogs += 5

if people >= dogs :
    print "People are greater then or equal to dogs."

if people <= dogs :
    print "People are less then or equal to dogs."

if people == dogs :
    print "People are dogs."