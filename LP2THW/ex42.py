#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第42题 物以类聚--CLASS 类
'''
你可以使用class这个关键字创建更棒的“函数字典”。
用到class的编程语言被称作Obje:ct Oriented Programming(OOP)（面向对象编程）
空客A330飞欧洲的。

stuff = ['Test','This','Out']#stuff 是一个「列表」“类”list class
print ' '.join(stuff)#' '（空格）是一个「字符串」类string class

还有一个概念，叫做 boject(物件)，创建几个 class后就会素娥到。怎么创建class呢？和创建ROOMS的方法差不多，但是其实跟家的简单：
'''
## 编程开始：下面的编程代码术语「升级版」
class TheThing(object):
# 报错：AttributeError: 'TheThing' object has no attribute 'number'

	def _init_(self):
		self.number = 0
	def some_function(self):
		print "I got called."
	def add_me_up(self,more):#Debug1,在more前面增加一个空格ok。
		self.number += more#报错debug，这个number没有attribute。检查未见异常。
		return self.number
		
		print self # 临时
		print more# 临时
		print self.number# 临时
		
# two different things
a = TheThing()#没有找到问题。
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)#报错debug，但是没有找到问题所在。
'''Traceback (most recent call last):
  File "/Users/yyy/Documents/Python_LP2THW/ex42.py", line 37, in <module>
    print a.add_me_up(20)#报错debug，但是没有找到问题所在。
  File "/Users/yyy/Documents/Python_LP2THW/ex42.py", line 23, in add_me_up
    self.number += more#报错debug，这个number没有attribute。检查未见异常。
AttributeError: 'TheThing' object has no attribute 'number'
'''
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number

# 作者的吐槽
'''
Python是个旧语言，包含很多丑陋的设计决定，为了掩盖，它们就做了新的丑陋设计，然后告诉人们让他们习惯这些新的坏设计。class TheTHing(object)就是其中一个例子。你也不用担心你为什么要在class后面添加一个（object），好吧，跟着做就是了。
你看到参数里的self么怼了，它就是Python
穿件的格外的参数，有了它你才能实现a.some_function()'这种用法，这时候他就会把\前者翻译成''some_function(a)执行下去。为什么用self呢？因为你的函数并不知道你的这个“实例”是来自一个叫做TheThing或者别的名字的class。所以你只要一用一个通用的名字self,这样你写出来的函数在任何情况下都能正常哦给你做了。
其实，你可以使用self意外的别的字眼，不过这样做的话，你就会成为其他程序员的众矢之的。只有变态才会在这里乱改。。对以后会读到你的代码的人好点，因为你现在的代码10年以后，所有的代码都会是一团糟。
接下来看到_init_函数了嘛？这就是你微Python class 设置内部变量的方式。你可以使用.将它们设置到self上面。另外看到我们使用了add_me_up()为你创建的self.number加值。后面你可以看到我们如何为数字加数值。

Class是很强大的东西，你应该好好读读相关的东西。金科鞥多找些东西读读，多多实验。你其实知道它们应该怎么用，只要试试就知道了，好吧下面使用class写一个练习。

好吧，下面我们将41题重写一遍。

'''
from sys import exit
from random import randint

class Game(object):

	def _init_(self,start):
		self.quips=[
			"You died. You kinda suck at this.",
			"Your mom would be pround.If she were smarter.",
			"Such a luser.",
			"I have a small puppy that's etter at this."]
		self.start = start
	def play(self):
		next = self.stat
		
		while True:
			print "\n------------"
			room =getattr(self,next)
			next = room()
# 我发现下面连续的定义的5个函数和ex41中至少是在名称和顺序上是一样的。
#在新的death()函数里，比上一个版本简洁的多。
# 在上一个版本里用到的是ROOMS = {  }这样的东西。多定义了一个函数def runner(），多了一个函数runner(参数ROOMS)
#在这个版本里声明了一个类：class Game(object)
#在这个版本里多了一个参数a_game，而且这个a_game还可以执行play()方法。	
	def death(self):
		print self.quips[randint(0,len(self.quips)-1)]
		exit(1)
		
	def central_corridor(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action =  raw_input("> ")
		
		
		if action == "shoot!":
			print "Quick n the draw you yank out your blaster and fire it at the Gothon."
			
			print "His clown costume is flowing and moivng around his body,which throws"
			
			print "off your aim.Your laser hits his costume but misses him entirely. This"
			
			print "completely ruins his brand new costume his mother bought him, which"
			
			print " makes him fly into an insane rage and blast you repeatedly in the face until"
			
			print "you are dead. Then he eats you."
			
			return 'death'
			
		elif action == "dodge!":
			print "Like a world class boxer you dodge,weave,slip and slide right"
			print "as the Gothon's blaser cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
			
	def laser_weapon_armory(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container. There's a keypad lock on the box"
		print "andyouneedthecodetogetthebombout. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits." 
		code = "%d%d%d" % (randint(1,9), randint(1,9),randint(1,9))
		guess = raw_input("[keypad]> ") 
		guesses = 0
		
		while guess !=code and guesses < 10:
			print "BZZZZZEDDDD!"
			guesses += 1
			guess = raw_input("[keypad]>")
		
		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the "
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
		
	def the_bridge(self):
		print "You burst onto the Bridge with the netron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "takecontroloftheship. Eachofthemhasan even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "In a pannic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Right as you drop it a "
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off." 
			return 'death'
		
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat." 
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "SOES NOT COMPUTE!"
			return "the_bridge"
			
	def escape_pod(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes. It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference. Yougettothechamberwiththe escape pods, and"
		print "now need to pick one to take. Some of them could be damaged"
		print "but you don't have time to look. There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button."% guess
			print "The pod escapes out into the void of space,then"
			print "implodes as the hull ruptures,crushing your body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to" 
			print "the planet below. As it flies to the planet,you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same" 
			print "time. You won!"
			exit(0)

a_game =Game("central_corridor")
a_game.play()

		



# 运行后的结果：
# 20171104注意，本文件的py代码并没有很好的通过“debug”，所以日后需要进一步调试，为了不行动瘫痪，我们将进入下一章ex43。

'''
这个版本的游戏和你的上一版效果应该是一样的，其实有些代码都几乎一样。比较一下两版代码，弄懂其中不同的地方，重点需要理解这些东西:

1. 怎样创建一个classGame(object)并且放函数到里边去。

2. __init__是一个特殊的初始方法，可以预设重要的变量在里边。

3. 为 class 添加函数的方法是将函数在 class 下再缩进一阶，class 的架构就是通过缩进实现的，这点很重要。

4. 你在函数里的内容又缩进了一阶。

5. 注意冒号的用法。

6. 理解self的概念，以及它在__init__、play、death里是怎样使用的。

7. 研究play里的getattr的功能，这样你就能明白play所做的事情。其实你可以手动在 Python命令行实验一下，从而弄懂它。

8. 最后我们怎样创建了一个Game，然后通过play()让所有的东西运行起来。


'''

# 加分题
'''
1. 研究一下__dict__是什么东西，应该怎样使用。

2. 再为游戏添加一些房间，确认自己已经学会使用 class 。

3. 创建一个新版本，里边使用两个 class，其中一个是Map，另一个是Engine。 
示:把play放到Engine里面。

'''


