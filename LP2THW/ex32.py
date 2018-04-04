#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第32题 循环和列表（for-loop）
'''
这里有个例子，关于列表：
hairs = ['brown','blond','red']#左方括号是“打开”列表，右括号是“结束”。将变量赋于等号左侧的变量。
eyes = ['brown','blue','green']
weights = [1,2,3,4]
'''
# 编程代码开始：
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
#this first kind of for-loop goes through a list

for number in the_count:
	print "This is count %d"%number

# same as above
for fruit in fruits:
	print "A fruit of type: %s"% fruit
	
#also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it 
for i in change:
	print"I got %r" % i

#we can also build listd,first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):#此处，可以将element赋值为range(0,6) 而无需使用for循环？
	print "Adding %d to the list."%i
	# append is a function that lists understand
	elements.append(i)#在Python文档中找到关于列表的内容，仔细阅读看看支持哪些操作？这里的操作是往列表变量elements中使用range()函数，依次添加。

# now we can print them out too
for i in elements:# 有没有发现，此处的循环函数中没有next。
	print "Element was: %d"%i


# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex32.py ============
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
>>> 


'''


