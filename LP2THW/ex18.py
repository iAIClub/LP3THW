#命名-变量-代码-函数（function）
#函数可以教你做3样事情：给代码片段命名；它们可以接受函数，就跟你的脚本接受argv一样；通过使用#1和#2，它们可以让你创建微型脚本或者小命令。
#你可以用def新建立函数，你现在学建立4个函数。
# 采用Python2.7自带的编辑器，他会提示时，在哪里输入个啥#*--UTF8---,这样编译的时候就不会出错了，直接在TextMate里编辑则会出错，容易报编码错误。

#this one is like your scripts with argv 这个函数和你的脚本里看到的argv带参数的变量是一个意思。
def print_two(*args):# A Function is defined。这里定义了个函数，「*args」是个什么鬼？为何要用*？
	arg1,arg2=args# 程序运行的时候需要输入两个参量arg1和arg2，这两个用户输入量会作为参量参与运行。
	print "arg1:%r,arg2:%r"%(arg1,arg2)
	
# ok,that *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):#这里多了一种打印两个用户输入内容的函数方法。这个函数可以跳过解包过程，追饿使用（）里边的名称作为变量名。
	print "arg1:%r,arg2:%r"%(arg1,arg2)
	
# this just takes one argument
def print_one(arg1):#仅仅打印一种用户输入参数arg1
	print "arg1:%r"%arg1
	
# this one takes no arguments
def print_none():#打印出
	print "I got nothin'."
	
print_two("Zed","Shaw")# 程序运行直接需要的两个输入参数，均用在这里了。
print_two_again("Zed","Shaw")# 这里貌似可以接受用户输入。
print_one("First!")
print_none()

# ················
'''
下面肢解以下print_two
1.首先我们高速Python，我要创建一个函数，用了命令def，也就是定义（define）的意思。
2.名字可以随便取，当然最好是能体现这个函数的功能，例如print_two.
3.我们告诉函数，我们需要* args，这个和脚本argv相似，参数必须放在（）中才能运行。
4.接着用「：」结束本行，下一行开始缩进。
5.冒号以下，前面缩进4个空格的，都属于这个函数的内容，第一行，用于-解包-
6.解包之后的每个参数打印出来，这样会显得更加清晰。

定义函数注意：
1.函数定义以def开始。
2.函数名称以字符和下划线组成。
3.函数名称紧跟着「（」
4.括号里包含多个参数，分别以逗号隔开。
5.不能使用重复的参数名。
6.参数最后要加入「）」、「：」和「？」
7.函数定义代码后新行要缩进4个格子
8.函数结束后要取消缩进。


使用函数注意：
1.调用函数（use或call）是否使用了函数的名称？
2.函数名称是否紧跟着「（？」
3.括号后又无参数？多个参数是否以逗号隔开？
4.函数是否以「）」结尾？
另注意：run、call和use函数是同一个意思。

'''
#················



'''
#以下是上述代码的运行结果#

Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex18.py ============
arg1:'Zed',arg2:'Shaw'
arg1:'Zed',arg2:'Shaw'
arg1:'First!'
I got nothin'.
>>> 
'''
