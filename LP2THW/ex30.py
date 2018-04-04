#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第30题:Else 和If
people=30

cars=40

buses=15


if cars> people:
	print"We should take the cars."#此行被打印。
elif cars< people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses< cars:# 此行被打印。
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright,let's just tkae the buses."#打印
else:
	print "Fine,let's stay home then."

# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex30.py ============
We should take the cars.
Maybe we could take the buses.
Alright,let's just tkae the buses.
>>> 
'''


