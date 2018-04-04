#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第25题 更多更多练习

def break_words(stuff):
	""" This function will break up words for us."""
	words= stuff.split(' ')#这里是啥意思？
	return words

def sort_words(words):#sort mean:make the sequence of words.
	""" Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off"""
	word=words.pop( 0 )#word to words
	print word
	
def print_last_word(words):
	"""Print the last word after poping it off."""
	word=words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words= break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words=break_words(sentence)#NameError: global name 'sentence' is not defined
#ex25.print_first_and_last(sentence):WRONG#at last ,the debug pass.
	#print_first_and_last(sentence):OK!whats wrong?
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sort the words then prints the first and last one."""
	words=sort_sentence(sentence)#This sentence can be debug nice，but the up one can not pass the debug。
	print_first_word(words)
	print_last_word(words)


# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex25.py ============
>>> 
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>>  sorted_words = ex25.sort_sentence(sentence)
 
  File "<pyshell#13>", line 2
    sorted_words = ex25.sort_sentence(sentence)
    ^
IndentationError: unexpected indent
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> 
'''





