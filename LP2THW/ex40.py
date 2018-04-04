#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第40题 字典，可爱的字典
'''
容器型数据结构——字典（dictionary）。这种数据类型在Python中叫"dict",有的语言里叫hash。注意它们和列表的区别。

你可以使用数字作为列表的索引，也就是你可以通过数字找到列表中的元素。而dict所做的，是让你可以通过任何东西找到元素，不只是数字。使得，子弟爱你可以将一个物体和另外的一个东西关联，不管他们的类型是什么。
'''
# 练习：
# 疑问，这个大括号{}和中括号[]在一个“字典”里是啥关系？
# 列表里用中括号[ ]?字典里用大括号{}?

cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

#上一行：大括号和小括号啥区别呢？将“字典”里的三个系列赋值给了cities.我现在看cities这个变量现在是以字典的格式存了一些东西，这些东西是以A：B的单元形式存储的，每个单元之间使用逗号“，”隔开。其中A是B的索引，也就说说通过pring cities['CA'] 可以打印出SanFrancisco来。而且这个“字典”里的元素是可以增删的，直接通过cities[Ai]="Bi"代码，可以把'Ai':'Bi'作为一组数据元素引入到字典中来，但是这一组数据是以什么样的顺序存在这个库里，就不得而知了。

# 背景知识：CA= California State of USA,SanFrancisco=旧金山、三藩市、圣弗朗西斯科，加州大学伯克利分校和斯坦福的所在地。NY是纽约州，MI是密西西比州的意思，州简称：对应的后面是这个州里最大的城市？

cities['NY']='New York'
#把字符串New York赋值给了NY ?不是的，这里的意思是将'NY':'New York'这一组数据 增加到cities这个字典里。

cities['OR']='Porland' 
# 把字符串 Porland 赋值给了OR？NO，这里的意思是，给你字典cities里面增加了新的一组数据  'OR':'Porland'

#对了，加完了之后，现在，这个cities字典的内容库就是{'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville','NY':'New York','OR':'Porland'}



def find_city(themap,state): #定义了一个函数，这个函数有2个参数：参数A和参数B

	if state in themap:# 如果参数2在参数1里,这里用到一个关键词in,查查怎么用。
		return themap[state]# 就返回 参数1# 这里明明要求的返回前一个参数的值，为啥运行的时候返回的是后一个参数的值？
		#我怎么记得中括号[]不是字典而是列表到意思呢？
		# 注意，在“字典”型变量的背后使用单个中括号[]的意思好像是要对其中一个元素动手。问题是temap{} 是个字典么？也许是，哪state是什么？其中一个元素？怎么看出来themap是个字典类的变量？ 
		#注意[ ]中的值是一个索引值么，看到前面的例子里也是 stuff={'name':'Zed'}  print stuff['name'] 返回的就是 Zed。
		#如果输入stuff[1]="Wow"，就是在原来的字典里增加了一条：1:'Wow'——这里返回的不是一个函数，这里themap[state]的意思是themap={'themap':'state'}，对？。这里的意思是，返回以state变量输入代表的这个字符串对应的元素，应该是temap{state:something?}我想这里的state其实是美国某个州的简称，比如CA。
		
		
	else:
		return "Not found."# 否则就返回NF

# ok pay attention!

cities['_find']=find_city# 注意：将字符串find_city 获得的一对值，赋值给_find？——例如CA？，就是说变成了cities['_find'](themap,state)，find_city；不对，这里的意思是往cities{A:B……}里增加一对数据？新增加了{A:B……_find:find_city}?


while True: #如果为真？谁为真？上面这一条？
	print"State?(ENTER to quit)",#打印出来：State？回车后取消。
	
	state= raw_input(">")#使用raw_input()函数，将“>”替代state
	
	if not state:break#如果state(>)后面不是break，这里有一个判断语句就是if not ***,这里state这个变量接受了用户在>后面的输入，state变量后面跟着：+break?这里怎么理解？是个什么意思？
	
	# this line is the most important ever!study!这一行最重要，注意注意注意！
	
	city_found = cities['_find'](cities,state) # 使用cities[_find'](其本质上是find_city ),即 find_city(cities,state)    citi_found这个变量的返回值有2种情况，1种是themap(citied), 另一种是Not found。如果state 是在cities里面的话，就返回cities[state]返回一个城市。
	#cities[ ] 是以「列表」而不是「字典」的形式来进行的，怎么进行的呢？列表后面紧跟[]（A，B）是怎么个意思？
	print city_found#city 有可能打字出来是citi
# 注意到我用了themap而不是map了吧？这是因为Python已经又一个函数叫做map了，如果你用map做变量，后面可能出问题。#这里只有两种情况了，或者是themap或者是Not Found.
	



# 运行后的结果：
'''
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex40.py ============
State?(ENTER to quit) >New York
Not found.
State?(ENTER to quit) >San Francisco
Not found.
State?(ENTER to quit) >MI
Detroit
State?(ENTER to quit) >CA
San Francisco
State?(ENTER to quit) >NY
New York
State?(ENTER to quit) >OR
Porland
State?(ENTER to quit) >FL
Jacksonville
State?(ENTER to quit) >
'''
#加分习题
'''
1. 在 Python 文档中找到 dictionary (又被称作 dicts, dict)的相关的内容，学着对 dict 做更多的操作。
2. 找出一些 dict 无法做到的事情。例如比较重要的一个就是 dict 的内容是无序的， 你可以检查一下看看是否真是这样。
3. 试着把for-loop执行到 dict 上面，然后试着在 for-loop 中使用 dict 的items()函数，看看会有什么样的结果。

'''
# LOG
# 20171101 用了比较多的心思来理解这些代码。


