#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/9 15:23
# @Author : wangchao
# @Site : 
# @File : ex38.py
# @Software: PyCharm

# Create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI',
}

# create a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-'*10
print "NY States has: ", cities['NY']
print "OR states has: ", cities['OR']

print '-' * 10
print "Michigan has: ", states['Michigan']
print "Florida has: ", states['Florida']
#print some states
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every states abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviation %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city  in cities.items():
    print "%s has the city %s " % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s " % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas',None)
if not state:
    print "Sorry, No Texas."

# get a city with a default value
city = cities.get('TX','Does not exists')
print "The city for the state 'TX' is: %s " % city
