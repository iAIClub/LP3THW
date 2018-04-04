#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第20题 函数和文件
from sys import argv# 从sys库中引入argv变量，包含2个参数

script, input_file = argv# argv变量包含2个参数，第一个是本程序名称，后一个是被引入的文件名。

def print_all(f):#定义一个函数，但是函数中的带的f是个啥。f是file的意思。
	print f.read()#f可以直接调用read()方法？这个是什么套路，忘了
	
def rewind(f):#定义里一个函数rewind?在这个函数里，依然使用了f参数，f参数可以直接调用seek()方法。
	f.seek(0)#f可以直接调用seek()函数
	
def print_a_line(line_count,f):#定义了一个新函数，函数的作用是打印一整行。函数中有2个参数，第一个参数是数数有几行，第几行？；第二个参数是f，但是f是个啥？传递一个变量。
	print line_count,f.readline()#打印一整行的这个函数中低你了打印两个东西，一个是行数，一个是数几行？

current_file=open(input_file)#这行带啊的意思是：引入一个current_file变量，通过open方法打开了input_file参数的这个文件。

print " First let's print the whole file:\n"# 打印一个字符串

print_all(current_file) #调用printall()这个函数，这里是打印所有的意思。

print "Now let's rewind,kind of like a tape."#打印一行字符串。

rewind(current_file)#调用一个rewind()函数,其实质是调用了一个叫做seek()的函数。

print "Let's print three lines:"

current_line=1#current_line变量被新赋予了一个数值1
print_a_line(current_line,current_file)

current_line=current_line+1#每运行一次，current_line变量会再+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)


# 运行后的结果：
'''
itifadeMacBook-Pro:~ yyy$ python  Documents/Python_LP2THW/ex20.py Documents/Python_LP2THW/test.txt
 First let's print the whole file:

How old are you?
How much do you earn?
Do you have children?

Now let's rewind,kind of like a tape.
Let's print three lines:
1 How old are you?

2 How much do you earn?

3 Do you have children?

itifadeMacBook-Pro:~ yyy$ 
'''


