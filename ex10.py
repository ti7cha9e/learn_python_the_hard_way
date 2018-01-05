#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 9:43
# @Author : wangchao
# @Site : 
# @File : ex10.py
# @Software: PyCharm

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i