#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第31题 作出决定
print "You enter a dark room with two doors.Do you go through door #1 or door #2?"

door = raw_input(">")

if door == "1":
	print "There's a giant bear here eating a cheese cake.What do you do ?"
	print "1.Take the cake."
	print "2.Scream at the bear."
	
	bear = raw_input(">")
	
	if bear=="1":#你可以在“if 语句”内部再放一个“if语句”。这是一个很强大的功能，可以用来创建嵌套(nested)的决定，其中的一个分支将引向另一个分支的子分支。
		print "The bear eats your face off.Good job!"
	elif bear=="2":
		print "The bear eats your legs off.Good job!"
	else:
		print"Well,doing %s is probably better.Bear runs away."% bear

elif door=="2":
	print "You stare into the endless abyss at Cthlhu's retina."
	print "1.Blueberries"
	print "2.Yellow jacket clothespins."
	print "3.Understanding revolvers yelling melodies."
	
	insanity = raw_input(">")
	
	if insanity =="1" or insanity =="2":
		print "Your body survives powered by a mind of jello.Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.Good job!"
else:
	print"You stumble around and fall on a knife and die.Good job!"




# 运行后的结果：
'''
It could fun freely nice！

'''


