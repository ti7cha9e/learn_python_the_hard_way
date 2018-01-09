#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/8 9:46
# @Author : wangchao
# @Site : 
# @File : ex25.py
# @Software: PyCharm

def break_words(stuff):
    """
    This function will break up words for us.
    """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    return word

def sort_setence(setence):
    """Take in a full setence and returns the sorted words"""
    words = break_words(setence)
    return sort_words(words)

def print_first_and_last(setence):
    """Prints the first and last words of the setence"""
    words = break_words(setence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(setence):
    """Sorts the words then prints the first and last one."""
    words = sort_setence(setence)
    print_first_word(words)
    print_last_word(words)

setence = "All good things come to those who wait."
words = break_words(setence)
print words
print sort_words(words)
print print_first_word(words)
print print_last_word(words)
print words
sorted_word = sort_words(words)
print print_first_word(sorted_word)
print print_last_word(sorted_word)
sorted_words = sort_setence(setence)
print sorted_words
print print_first_and_last(setence)
print print_first_and_last_sorted(setence)