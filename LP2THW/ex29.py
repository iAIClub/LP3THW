#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第29题 if 语句
people=20
cats=30
dogs=15


if people < cats:
	print"Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people>=dogs:
	print "People are greater than or equal to dogs."
	
if people<= dogs:
	print"People are less than or equal to dogs."
	

if people==dogs:
	print"People are dogs."

# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex29.py ============
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
>>> 


'''


