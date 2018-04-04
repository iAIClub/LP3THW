#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第35题 分支和函数

from sys import exit #从sys库里引入exit模组？

def glod_room():#定义了一个函数，名为glod_room(),
	print"This room is full of gold. How much do you take?"
	
	next = raw_input(">")
	if  "0" in next or "1" in next:#这里为啥是0和1？如果不是0 或者1呢？
		how_much = int(next)
	else:
		dead("Man,learn to type a number.")#这里定义过dead()函数吗？
		
	if how_much< 50:
		print"Nice,you're not greedy,you win!"
		exit(0)#exit()函数怎么用？exit(0)有什么意义？
	else:
		dead("You greedy bastard!")

		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"#?
	bear_moved=False
	
	while True:
		next = raw_input (">")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next=="taunt bear" and not bear_moved:
			print "The bear has moved from the door.You can go through it now."
			bear_moved= True
		elif next=="taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next=="open door" and bear_moved:
			glod_room()
		else:
			print"I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He,it,whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
		
def dead(why):
	print why ,"Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next= raw_input(">")
	
	if next == "left":
		bear_room()#
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room untill you starve.")


start ()#
	






# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex35.py ============
You are in a dark room.
There is a door to your right and left.
Which one do you take?
>left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
>taunt bear
The bear has moved from the door.You can go through it now.
>open door
This room is full of gold. How much do you take?
>ak47
Man,learn to type a number. Good job!
>>> 

'''
#加分习题:

'''
1. 把这个游戏的地图画出来，把自己的路线也画出来。 

2. 改正你所有的错误，包括拼写错误。

3. 为你不懂的函数写注解。记得文档注解该怎么写吗?

4. 为游戏添加更多元素。通过怎样的方式可以简化并且扩展游戏的功能呢?

5. 这个 gold_room 游戏使用了奇怪的方式让你键入一个数字。这种方式会导致什么
样的 bug? 你可以用比检查 0、1 更好的方式判断输入是否是数字吗?int()这 个函数可以给你一些头绪。

'''
# 我的常见错误：
'''
在我输入这些代码的时候，我经常会把False输错成Flase,立此存照，以后要改过来。
'''

