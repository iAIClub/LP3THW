#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第41题 来自 Percal25号行星的哥顿人（Gothons）
# 上一节里你发现了dict的秘密功能了嘛，你可以解释给自己听嘛？好吧，让我来给你解释一下：
'''
cities['_find']= find_city
city_found= cities['_find'](cities,state)
#你要记住一个函数也可以作为一个变量，"def find_city"创建了一个可以在任何地方都能使用的变量。在这段代码里，我们把
'''


#原文内容
#作者其实想告诉你的是，你可以使用剥开洋葱等方法把代码读透彻。
 
#∂∂ƒ©åEEßß∂ƒ©˙∂´®†¥¨ˆππ“““øΩ”””˙∆˚¬…¬…¬¬¬¬………æææ  µ˜µ˜∫√ç≈Ωåœœ∑

'''
你要记住一个函数也可以作为一个变量，``def find_city`` 比如这一句创建了一 个你可以在任何地方都能使用的变量。在这段代码里，我们首先把函数 find_city 放到叫做 cities 的字典中，并将其标记为 '_find'。 这和我们将 州和市关联起来的代码做的事情一样，只不过我们在这里放了一个函数的名称。
好了，所以一旦我们知道 find_city 是在字典中 _find 的位置，这就意味着我 们可以去调用它。第二行代码可以分解成如下步骤:
1. Python 看到 city_found = 于是知道了需要创建一个变量。
2. 然后它读到cities，然后知道了它是一个字典
3. 然后看到了['_find']，于是 Python 就从索引找到了字典cities中对应的位
  置，并且获取了该位置的内容。
4. ['_find']这个位置的内容是我们的函数find_city，所以 Python 就知道了
这里表示一个函数，于是当它碰到 ( 就开始了函数调用。
5. 这两个参数将被传递到函数 中，然后这个函数就被
   cities, state
find_city
运行了。
6. find_city接着从cities中寻找states，并且返回它找到的内容，如果什么
都没找到，就返回一个信息说它什么都没找到。
7. Python find_city 接受返回的信息，最后将该信息赋值给一开始
的   这个变量。
city_found
 我再教你一个小技巧。如果你倒着阅读的话，代码可能会变得更容易理解。让我 们来试一下，一样是那行:
1. state和city是... 2. 作为参数传递给...
3. 一个函数，位置在...
132
					  
4. '_find'然后寻找，目的地为... 5. cities这个位置...
6. 最后赋值给city_found.
还有一种方法读它，这回是“由里向外”。
1. 找到表达式的中心位置，此次为['_find'].
2. 逆时针追溯，首先看到的是一个叫cities的字典，这样就知道了 cities 中
的 _find 元素。
3. 上一步得到一个函数。继续逆时针寻找，看到的是参数。
4. 参数传递给函数后，函数会返回一个值。然后再逆时针寻找。
5. 最后，我们到了city_found=的赋值位置，并且得到了最终结果。
 数十年的编程下来，我在读代码的过程中已经用不到上面的三种方法了。我只要 瞟一眼就能知道它的意思。甚至给我一整页的代码，我也可以一眼瞄出里边的 bug 和错误。这样的技能是花了超乎常人的时间和精力才锻炼得来的。在磨练 的过程中，我学会了下面三种读代码的方法，它们是用户几乎所有的编程语言:
1. 从前向后。 2. 从后向前。 3. 逆时针方向。
 下次碰到难懂的语句时，你可以试试这三种方法。
'''
# 代码部分
from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
			 "NIce job, you died ...jackass.",
			 "Sunch a luser.",
			 "I have a small puppy that's better at this."]
	
	print quips[ randint(0,len(quips)-1)]
	exit(1)
	
def central_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed "
	print "your entire crew. You are the last surviving member and your last"
	print "mission is to get thr neutron destruct bomb from the Weapons Armory,"
	print "put it in the bridge,and blow the ship up after getting into an "
	print "escape pod."
	print "\n"
	print "You're running down the central corridor to the Weapons Armory when"
	print "a Gothon jumps out ,red scaly skin,dark grimy teeth,and evil clown costume"
	print "flowing around his hate filled body.He's blocking the door to the"
	print "Armory and about to pull aweapon to blast you."
	
	action = raw_input(">")
	
	if action =="shoot!":
		print "Quick on the draw you yank out your blaster and fire it at the Gothon."
		print "His clown costume is flowing and moving around his body,which throws"
		print "off your aim.Your laser hits his costume but misses him entirely. This"
		print "completely  ruins his brand new costume his mother bought him,which"
		print "makes him fly into an insane rage and blast you repeatly in the face until"
		print "you are dead.Then he eats you."
		return 'death'
		
	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave,slip and slider right"
		print " as the Gothon's blaster cranks a laser past your head."
		print " In the middle of your artful dodge your foot slips an you"
		print " bang  your head on the metal wall and pass out."
		print "You wake up shortly after only to die as the Gothon stomps on"
		print "your head and eats you."
		return 'death'
		
	elif action == "tell a joke":
		print "Lucky for you they made you learn Gothon insults in the academy."
		print "You tell the one Gothon joke you know:"
		print "Lbhe zbgure vf fb sng , jura fur fvgf nebhaq qurbuhfr ,fur fvgf nebhaq qur ubhfr."
		print "The Gothin stops,tries not to laugh,then busts out lauging and can't move."
		print "While he's laughing you run up and shoot him square in the head"
		print "putting him down,then jump through the Weapen Armory door."
		return 'laser_weapon_armory'
		
	else:
		print "DOES NOT COMPUTR!"
		return 'central_corridor'
		
def laser_weapon_armory():
	print "You do a dive roll into the Weapon Armory,crouch and scan the room"
	print "for more Gothons that might be hiding.It's dead quiet,too quiet."
	print "You stand up and run to the far side of the rom and find the "
	print "neutron bomb in its container.There's a keypad lock on the box"
	print "and you need the code to get the bomb out.If you get the code"
	print "wrong 10 times then the lock closes forever and you can't"
	print "get the bomb.The code is 3 digits."
	code ="%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))
	guess= raw_input("[keypad]>")
	guesses = 0 #guess后面加复数es
	print "the guess is "+ guess
	print "the code is "+code
	while guess != code and guesses < 10:
		print "BZZZZEDDD!"
		guesses += 1
		guess =  raw_input("[keypad]>")
		
	if guess == code:
		print "The container clicks open and the seal breaks,letting gas out."
		print "You grab the neutron bomb and run as fast as you can to the"
		print "bridge where you must place it in the right spot."
		return 'the_bridge'
	else:
		print "The lock buzzes one last time and then you hear a sickening"
		print "melting sound as the mechanism is fused together."
		print "You decide to sit there,and finally the Gothons blow up the"
		print "ship from their ship and you die."
		return 'death'
		
def the_bridge():
	print "You burst onto the Bridge with the neutron destruct bomb"
	print "under your arm and surprise 5 Gothons who are trying to "
	print "take control of the ship.Each of them has an even uglier"
	print "clown costume than the last.The have't pulled their"
	print "weapons out yet,as they see the active bomb under your"
	print "arm and don't want to set it off."
	
	action =raw_input("> ")
	
	if action == "throw the bomb":
		print "In a panic you throw the bomb at the group of Gothons"
		print "and make aleap for the door.Right as you drop it a"
		print "Gothon shoots you right in the back killing you."
		print "As you die as you see another Gothon frantically try to disarm"
		print "the bomb.You die knowing they will pribably blow up when"
		print "it goes off."
		return 'death'
	
	elif action == "slowly place the bomb":
		print "You point your blaster at the bomb under your arm"
		print "and the Gothons put their hands up and start to sweat."
		print "You inch backward to the door,open it,and then carefully"
		print "place the bomb on the floor,pointing your blaster ast it."
		print "You then jump back through the door,punch the close button"
		print "and blast the lock so the Gothons can't get our."
		print "Now that the bomb is placed you run to the escape pod to "
		print " get off this tin can."
		return 'escape_pod'
	else:
		print "DOES NOT COMPUTE!"
		return "the_bridge"

def escape_pod():
	print "You rush through the ship desperately trying to make it to "
	print "the escape pod before the whole ship explodes. It seems like "
	print "hardly any Gothons are on the ship, so your run is clear of "
	print "interference.You get to the chamber with the escape pods, and"
	print "now need to pick one to take. Some of them could be damaged"
	print "but you don't have time to look.There's 5 pods,which one"
	print "do you take ?"
	
	good_pod =randint(1,5)
	guess = raw_input("[pod #]>")
	
	
	if int(guess) != good_pod:
		print "You jump into pod %s and hit the eject button."%guess
		print "The pod escapes out into the void of space,then"
		print "implodes as the hull ruptures, crushing your body"
		print "into jam jelly."
		return 'death'
	else:
		print "You jump into pod %s and hit the eject button."%guess
		print "The pod easily slides out into space heading to"
		print "the planet below. As it flies to the planet,you look"
		print " back and see your ship implode then explode like a "
		print "bright star,taking out the Gothon ship at the same"
		print "time.You won!"
		exit(0)
		
		
ROOMS = {
	'death':death,
	'central_corridor':central_corridor,
	'laser_weapon_armory':laser_weapon_armory,
	'the_bridge':the_bridge,
	'escape_pod':escape_pod
	}
	
	
def runner(map, start):
	next = start
	
	while True:
		room = map[next]
		print "\n---------"
		next = room()
	
runner(ROOMS, 'central_corridor')#没看出来哪里又问题，增加个空格看看行不行。


	








# 运行后的结果：
'''
---------第3次运行结果-----------

Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/yyy/Documents/Python_LP2THW/ex41.py ============

---------
The Gothons of Planet Percal #25 have invaded your ship and destroyed 
your entire crew. You are the last surviving member and your last
mission is to get thr neutron destruct bomb from the Weapons Armory,
put it in the bridge,and blow the ship up after getting into an 
escape pod.


You're running down the central corridor to the Weapons Armory when
a Gothon jumps out ,red scaly skin,dark grimy teeth,and evil clown costume
flowing around his hate filled body.He's blocking the door to the
Armory and about to pull aweapon to blast you.
>tell a joke
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng , jura fur fvgf nebhaq qurbuhfr ,fur fvgf nebhaq qur ubhfr.
The Gothin stops,tries not to laugh,then busts out lauging and can't move.
While he's laughing you run up and shoot him square in the head
putting him down,then jump through the Weapen Armory door.

---------
You do a dive roll into the Weapon Armory,crouch and scan the room
for more Gothons that might be hiding.It's dead quiet,too quiet.
You stand up and run to the far side of the rom and find the 
neutron bomb in its container.There's a keypad lock on the box
and you need the code to get the bomb out.If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.The code is 3 digits.
[keypad]>test
the guess is test
the code is 823
BZZZZEDDD!
[keypad]>456
BZZZZEDDD!
[keypad]>823
The container clicks open and the seal breaks,letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

---------
You burst onto the Bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to 
take control of the ship.Each of them has an even uglier
clown costume than the last.The have't pulled their
weapons out yet,as they see the active bomb under your
arm and don't want to set it off.
> 


--------------第3次完成--------------
'''
# 加分习题[暂时没做]
'''
1. 解释一下返回至下一个房间的工作原理。
2. 创建更多的房间，让游戏规模变大。
3. 除了让每个函数打印自己以外，再学习一下“文档字符串(docstrings)”式的注解。看
看你能不能将房间 述写成文档注解，然后修改运行它的代码，让它把文档注解打
印出来。
4. 一旦你用了文档注解作为房间 述，你还需要让这个函数打印出用户 示吗?试着
让运行函数的代码打出用户 示来，然后将用户输入传递到各个函数。你的函数应
该只是一些 if 语句组合，将结果打印出来，并且返回下一个房间。
5. 这其实是一个小版本的“有限状态机(finitestatemachine)”，找资料阅读了解一下，
  虽然你可能看不懂，但还是找来看看吧。
'''
