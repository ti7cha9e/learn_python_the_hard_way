#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 9:03
# @Author : wangchao
# @Site : 
# @File : ex8.py
# @Software: PyCharm

formater = "%r %r %r %r"

print formater % (1,2,3,4)
print formater % ("one", "two", "three", "four")
print formater % (True, False, False, True)
print formater % (formater, formater, formater, formater)
print formater % (
    "I had this things.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)