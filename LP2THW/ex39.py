#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第39题 列表的操作
''''
你看到像mystuff.append('hello')这样的代码，实际上在Python内部激发了一个连锁反应。原理：
括号-（parenthesis）
append(mustuff,'hello')==mystuff.append('hello')

'''
# 练习
ten_things="Apples Oranges Crow Telephone Light Sugar"

print "Wait there's not 10 things in that list,let's fix that."

stuff = ten_things.split(' ')
more_stuff =["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!=10:
	next_one = more_stuff.pop()
	print"Adding:",next_one
	stuff.append(next_one)
	print "There's %d item now."% len(stuff)
	
print "There we go:",stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]#whoa! fancy
print stuff.pop()
print ' '.join(stuff)# what? cool?
print '#'.join(stuff[3:5])#super stellar!


# 运行后的结果：

'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex39.py ============
Wait there's not 10 things in that list,let's fix that.
Adding: Boy
There's 7 item now.
Adding: Girl
There's 8 item now.
Adding: Banana
There's 9 item now.
Adding: Corn
There's 10 item now.
There we go: ['Apples', 'Oranges', 'Crow', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crow Telephone Light Sugar Boy Girl Banana
Telephone#Light
>>> 
======
# 加分题
加分习题
1. 将每一个被调用的函数以上述的方式翻译成 Python 实际执行的动作。例 如: ' '.join(things) 其实是 join(' ', things) 。
2. 将这两种方式翻译为自然语言。例如，   可以翻译成“用 ‘ ‘ 连
' '.join(things)
接(join) things”，而 join(' ', things) 的意思是“为 ‘ ‘ 和 things 调用 join
函数”。这其实是同一件事情。
3. 上网阅读一些关于“面向对象编程(ObjectOrientedProgramming)”的资料。晕了吧?
嗯，我以前也是。别担心。你将从这本书学到足够用的关于面向对象编程的基础知
  识，而以后你还可以慢慢学到更多。
4. 查一下 Python 中的 “class” 是什么东西。不要阅读关于其他语言的 “class” 的用
法，这会让你更糊涂。
5. dir(something)和something的 class 有什么关系?
6. 如果你不知道我讲的是些什么东西，别担心。程序员为了显得自己聪明，于是就发
明了 Opject Oriented Programming，简称为 OOP，然后他们就开始滥用这个东西 了。如果你觉得这东西太难，你可以开始学一下 “函数编程(functional programming)”。


'''


