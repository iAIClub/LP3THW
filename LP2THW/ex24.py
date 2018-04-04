#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第24题 更多练习

print "Let's practice everything."
print 'You\'d need to know \' bout escapes with \\ that do \n newlines and \t tabs.'#\是个转义字符，意思说：嘿 我后面这个 '单引号是个单独的单引号，不能和前面后面的单引号结合组成什么引号组。两个\\时候，前面的那个\是个转义字符，后面这个是被转意的对象；\n 这个转义字符不仅仅是转换意思的作用，更重要的是\n代表了新起一行；\t代表往后退一格。


poem = """
\tThe Lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t where there is none.
"""#注意连续的三对双引号是用来饮用一段文字的。忘记\t是啥意思了，但是从打印出来的样子来看前面是空出来几个格的。在源代码段落里新起的一行，其打印出来的样子依然是另起一行。但是，如果在代码里，同一行里如果出来了\n则在打印的时候会单独起一行。\n\t连用的时候，代表另起一行，并且前面空出几个格？

print "----------------------"
print poem
print "----------------------"

five= 10-2+3-6
print"This should be five: %s"% five#这里还是说占位符的事，在字符串里包含一个占位符，这个占位符是带格式的，注意后面是%加一个变量。

def secret_formula(started):#这里定义了一个函数secret_formula()
	jelly_beans= started*500#下面制造了3个变量jelly_beans,jars,crates，函数要求输入一个值started,函数最后返回了3个值。
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates
	
start_point= 10000
#定义了一个变量名称为start_point的变量，这个变量被赋予了一个值。这个值被secret_formula()函数作为输入量引用，返回的三个量分别存在beans(和上面代码里的jelly_beans是啥关系？)、jars、crates中。
beans,jars,crates= secret_formula(start_point)

print "With a starting point of: %d"% start_point#start_point变量可以被引用到代码中。
print "We'd have %d beans,%d jars, and %d crates."%(beans,jars,crates)#上面的三个变量获得了值之后，分别赋给了3个变量。这3个变量外面包含了括号。

start_point = start_point/10#这里把start_point变量变为原来的1/10.

print "We can also do that this way:"
print "We'd have %d beans,%d jars,and %d crates."%secret_formula(start_point)#这里用函数返回的三个数值，外面不包含括号。


# 运行后的结果：
'''
============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex24.py ============
Let's practice everything.
You'd need to know ' bout escapes with \ that do 
 newlines and 	 tabs.
----------------------

	The Lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

	 where there is none.

----------------------
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans,5000 jars, and 50 crates.
We can also do that this way:
We'd have 500000 beans,500 jars,and 5 crates.
>>> ∂
'''


