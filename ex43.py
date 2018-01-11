#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/10 10:12
# @Author : wangchao
# @Site : 
# @File : ex43.py
# @Software: PyCharm

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class ###(###): ":"Make a class named ### that is-a ###.",
    "class ###(object):\n\tdef __init__(self, ***)":"class ### has-a __init__ that take self and *** parameters.",
    "class ###(object):\n\tdef ***(self, @@@)":"class ### has-a function named *** that take self and @@@ parameters.",
    "*** = ###()":"set *** to an instance of class ###.",
    "***.***(@@@)":"From *** get the *** function, and call it wiht parameters self, @@@.",
    "***.*** = '***'":"From *** get the *** attribute and set it to '***'",
}

# do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readline():
    WORDS.append(word.strip().decode())
    #print WORDS

def convert(snippet, phrase):
    class_names = [ w.capitalize() for w in random.sample(WORDS, snippet.count('###'))]
    other_names = random.sample(WORDS, snippet.count('***'))
    results = []
    param_names = []

    for i in range(0, snippet.count('@@@')):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for setence in snippet, phrase:
        result = setence [:]

        for word in class_names:
            result = result.replace("###", word, 1)

        for word in other_names:
            result = result.replace('***', word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return  results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            pharese = PHRASES[snippet]
            question, answer = convert(snippet, pharese)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print ("ANSWER: %s\n\n " % answer)
except EOFError:
    print "\nBye!"