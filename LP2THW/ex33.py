#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第33题 While循环（while-loop循环）
'''
如果，某一行是以冒号（colon）结尾，意味着接下来的内容是一个新的代码片段，新的代码片段是需要被缩进的。
上一题说是for loop循环，但是实际上并没有发现loop。
本题诗练习 while-loop循环，这里说到while有一个问题就是有时候它永远不会结束，所以做了如下规定：
1尽量少用while-loop,大部分时候使用for-loop比较好。
2重复检查你的while 语句，确保布尔表达式最终会变成False
3如果不确定，就在while-loop结尾打印出你想要测试的值，看看变化
'''
# 好了，现在开始编程

i=0

numbers=[]

while i < 6:
	print "At the top i is %d"% i
	numbers.append(i)
	i = i + 1
	print "Number now:",numbers
	print "At the bottom i is %d"% i

print  "The numbers:"

for num in numbers:
	print num



# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex33.py ============
At the top i is 0
Number now: [0]
At the bottom i is 1
At the top i is 1
Number now: [0, 1]
At the bottom i is 2
At the top i is 2
Number now: [0, 1, 2]
At the bottom i is 3
At the top i is 3
Number now: [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Number now: [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Number now: [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers:
0
1
2
3
4
5
>>> 
'''
#加分习题
#> 下述加分题，并没有做，将来再刷的时候再做吧？
''''
1. 将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。 2. 使用这个函数重写你的脚本，并用不同的数字进行测试。
 
3. 为函数添加另外一个参数，这个参数用来定义第 8 行的加值 + 1 ，这样你就可以 让它任意加值了。
4. 再使用该函数重写一遍这个脚本。看看效果如何。
5. 接下来使用 for-loop 和 range 把这个脚本再写一遍。你还需要中间的加值操作
  吗?如果你不去掉它，会有什么样的结果?

# 解释：很有可能你会碰到程序跑着停不下来了，这时你只要按着 CTRL 再敲 c (CTRL-c)， 这样程序就会中断下来了。
# 加分题：
'''


