# -*- coding: utf-8 -*-
# 19:函数和变量

#注意，函数里的变量和脚本里的变量是没有任何关系的。

# 下面开始编程

def cheese_and_crackers (cheese_count,boxes_of_crackers):
	print "You have %d cheeses!"% cheese_count
	print "You have %d boxes of crackers!"%boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"#\n在这里起了个啥作用？
	
print "We can just give the function number directly:"
cheese_and_crackers(20,30)

print "OR,we can use variables from our script:"
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can evern do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers +1000)

'''
运行后的结果：
>>> 
============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex19.py ============
We can just give the function number directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR,we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can evern do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two,variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.

>>> 
'''
