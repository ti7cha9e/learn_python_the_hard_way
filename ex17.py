#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/5 13:17
# @Author : wangchao
# @Site : 
# @File : ex17.py
# @Software: PyCharm

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

#we
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done!"

out_file.close()
in_file.close()