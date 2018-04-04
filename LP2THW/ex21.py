#!/usr/bin/python
# -*- coding: utf-8 -*-
#第21题
# 学会用return来将变量设置为“一个函数的值”
def add(a,b):
	print "ADDING %d + %d"%(a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d-%d"%(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLYING %d * %d"%(a,b)
	return a*b

def divide(a,b):
	print "DIVIDING %d/%d"%(a,b)
	return a/b

print "Let's do some math with just functions!"

age = add(30,5)

height= subtract(78,4)

weight=multiply(90,2)

iq=divide(100,2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d"%(age,height,weight,iq)

# A puzzle for the extra credit,type it in anyway.
print "Here is a puzzle."
what=add(age,subtract(height,multiply(weight,divide(iq,2))))#这里是函数套函数，以某个函数的返回值当作输入参量。

print "That becomes:",what,"Can you do it by hand?"


# 以下是代码运行后所显示的结果
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex21.py ============
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78-4
MULTIPLYING 90 * 2
DIVIDING 100/2
Age:35,Height:74,Weight:180,IQ:50
Here is a puzzle.
DIVIDING 50/2
MULTIPLYING 180 * 25
SUBTRACTING 74-4500
ADDING 35 + -4426
That becomes: -4391 Can you do it by hand?
>>> 
'''