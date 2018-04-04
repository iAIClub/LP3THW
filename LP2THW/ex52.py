#!/usr/bin/python
# -*- coding: utf-8 -*-

# 第52题 创建你的web游戏

# 以下是{文章文字}部分
''''
这本书马上就要结束了。本章的练习对你是一个真正的挑战。当你完成以后，你 就可以算是一个能力不错的 Python 初学者了。为了进一步学习，你还需要多 读一些书，多写一些程序，不过你已经具备进一步学习的技能了。接下来的学习 就只是时间、动力、以及资源的问题了。
在本章习题中，我们不会去创建一个完整的游戏，取而代之的是我们会为《习题 42》中的游戏创建一个“引擎(engine)”，让这个游戏能够在浏览器中运行起来。
这会涉及到将《习题 42》中的游戏“重构(refactor)”，将《习题 47》中的架构混 合进来，添加自动测试代码，最后创建一个可以运行游戏的 web 引擎。
这是一节很庞大的习题。我预测你要花一周到一个月才能完成它。最好的方法是 一点一点来，每晚上完成一点，在进行下一步之前确认上一步有正确完成。
'''


# 重构 ex42的游戏
'''
你已经在两个练习中修改了 gothonweb 项目，这节习题中你会再修改一次。这 种修改的技术叫做“重构(refactoring)”，或者用我喜欢的讲法来说，叫“修修补补 (fixing stuff)”。重构是一个编程术语，它指的是清理旧代码或者为旧代码添加新 功能的过程。你其实已经做过这样的事情了，只不过不知道这个术语而已。这是 写软件过程的第二个自然属性。
你在本节中要做的，是将《习题 47》中的可以测试的房间地图，以及《习题 42》 中的游戏这两样东西归并到一起，创建一个新的游戏架构。游戏的内容不会发生 变化，只不过我们会通过“重构”让它有一个更好的架构而已。

 第一步是将ex47/game.py的内容复制到gothonweb/map.py中，然后将
tests/ex47_tests.py的内容复制到tests/map_tests.py中，然后再次运行nosetests，确认他们还能正常工作。

Note：
从现在开始我不会再向你展示运行测试的输出了，我就假设你回去运行这些测试，
 而且知道怎样的输出是正确的。

'''
## 架构
''''
将《习题 47》的代码拷贝完毕后，你就该开始重构它，让它包含《习题 42》 中的地图。我一开始会把基本架构为你准备好，然后你需要去完成map.py
和map_tests.py 里边的内容。
 首先要做的是使用 Room类来构建基本的地图架构:
'''
class Room(object):
	
	def __init__(self, name, description):
		self.name =name
		self.description = description
		self.paths = {}
		
	def go(self,direction):
		return self.paths.get(direction,None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
central_corridor = Room ("Central Corridor",

"""
The Gothons of Planet Percal #25 have invaded your ship and
destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.
You're running down the central corridor to the Weapons Armory
when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowingaroundhishatefilledbody. He'sblockingthedoor to the
Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
 """
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the
head
putting him down, then jump through the Weapon Armory door.
You do a dive roll into the Weapon Armory, crouch and scan the room
formoreGothonsthatmightbehiding. It'sdeadquiet,too quiet.
You stand up and run to the far side of the room and find the neutronbombinitscontainer. There'sakeypadlockonthebox
andyouneedthecodetogetthebombout. Ifyougetthecode wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits.
"""
)

the_bridge = Room("The Bridge", """
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.
You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off.
""")

escape_pod = Room("Escape Pod", """You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to get off this tin can.
You rush through the ship desperately trying to make it to
theescapepodbeforethewholeshipexplodes. Itseemslike
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods, and
nowneedtopickonetotake. Someofthemcouldbedamaged but you don't have time to look. There's 5 pods, which one do you take?
""")
the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below. As it flies to the planet, you lookback and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same time. You won!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button. The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.
"""
)

escape_pod.add_paths({ '2': the_end_winner,
'*': the_end_loser })

generic_death = Room("death", "You died.")
the_bridge.add_paths({
'throw the bomb': generic_death, 'slowly place the bomb': escape_pod
})
laser_weapon_armory.add_paths({
'0132': the_bridge,
'*': generic_death
})

central_corridor.add_paths({ 'shoot!': generic_death, 'dodge!': generic_death,
'tell a joke': laser_weapon_armory
})

START = central_corridor

# 我们会发现我们的 Room 类和地图存在一些问题
'''
  1. 在进入一个房间以前会打印出一段文字作为房间的 述，我们需要将这些 述和每 个房间关联起来，这样房间的次序就不会被打乱了，这对我们的游戏是一件好事。这些 述本来是在 if-else 结构中的，这是我们后面要修改的东西。
  2.原版游戏中我们使用了专门的代码来生成一些内容，例如炸弹的激活键码，舰舱的 选择等，这次我们做游戏时就先使用默认值好了，不过后面的加分习题里，我会要
    求你把这些功能再加到游戏中。
 3. 我为所有的游戏中的失败结尾写了一个generic_death，你需要去补全这个函数。
 你需要把原版游戏中所有的失败结尾都加进去，并确保代码能正确运行。
 4. 我添加了一种新的转换模式，以"*"为标记，用来在游戏引擎中实现“catch-all”动
 作。
 
  等你把上面的代码基本写好以后，接下来就是引导你继续写下去的自动测试的内容 tests/map_test.py 了:
'''

from nose.tools import *
from gothonweb.map import *

def test_room():
	gold = Room("GoldRoom",
"""This room has gold in it you can grab.There's a
door to the north.""") 
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
	
def test_room_paths():
	center = Room("Center", "Test room in the center.") 
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	center.add_paths({'north': north, 'south': south})
	
	assert_equal(center.go('north'), north) 
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	start.add_paths({'west': west, 'down': down}) 
	west.add_paths({'east': start}) 
	down.add_paths({'up': start})
	assert_equal(start.go('west'), west) 
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
	
def test_gothon_game_map(): 
	assert_equal(START.go('shoot!'), generic_death)
	assert_equal(START.go('dodge!'), generic_death)
	room = START.go('tell a joke') 
	assert_equal(room, laser_weapon_armory)
	
''''
你在这部分练习中的任务是完成地图，并且让自动测试可以完整地检查过整个地
图。这包括将所有的 generic_death 对象修正为游戏中实际的失败结尾。让你 的代码成功运行起来，并让你的测试越全面越好。后面我们会对地图做一些修改， 到时候这些测试将保证修改后的代码还可以正常工作。
'''
# 会话（session）和用户跟踪
'''
在你的 web 程序运行的某个位置，你需要追踪一些信息，并将这些信息和用户 的浏览器关联起来。在 HTTP 协议的框架中，web 环境是“无状态(stateless)” 的，这意味着你的每一次请求和你其它的请求都是相互独立的。如果你请求了页 面 A，输入了一些数据，然后点了一个页面 B 的链接，那你在页面 A 输入的 数据就全部消失了。
'''
####解决问题的方法
''''
解决这个问题的方法是为 web 程序建立一个很小的数据存储功能，给每个浏览 器进程赋予一个独一无二的数字，用来跟踪浏览器所作的事情。这个存储通常用 数据库或者存储在磁盘上的文件来实现。在 lpthw.web 这个小框架中实现这样 的功能是很容易的，以下就是一个这样的例子:
'''

import web

web.config.debug = False

urls = (
	"/count", "count", 
	"/reset", "reset"
)
app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count': 0})


class count:
	def GET(self):
		session.count += 1
		return str(session.count)


class reset:
	def GET(self):
		session.kill() 
		return " "
		
if __name__ == "__main__":
app.run()

''''
为了实现这个功能，你需要创建一个sessions/ 文件夹作为程序的会话存储位置，建好以后运行合格程序，然后检查/coint 页面，刷新一下这个页面看看计数会不会累加上去。关掉浏览器，程序就会“忘掉”之前的位置，这也是我们的游戏所需的功能。有一种方法可以让浏览器永远记住一些信息，不过这回让测试和开发变得更困难。如果你回到/reset/ 页面，然后在访问/count 页面，你可以看到你的计数器被重置了，因为你已经把会话傻掉了。

你需要花点时间弄懂这段代码，注意会话开始时 count 值是如何设定为0 的，另外再看看 session/ 下面的文件，看看你能不能把他们打开。下面是我把一个 Python 会话打开并且解码的过程：

>>> import pickle
>>> import base64
>>> base64.b64decode(open("sessions/XXXXX").read())
"(dp1\nS'count'\np2\nI1\nsS'ip'\np3\nV127.0.0.1\np4\nsS' session_id'\np5\nS'XXXX'\np6\ns."
>>>
>>> x = base64.b64decode(open("sessions/XXXXX").read())
>>>
>>> pickle.loads(x)
{'count': 1, 'ip': u'127.0.0.1', 'session_id': 'XXXXX'}

 所以会话其实就是使用   和   这些库写到磁盘上的字典。存储和管 理会话的方法很多，大概和 Python 的 web 框架那么多，所以了解它们的工作 原理并不重要。当然如果你需要调试或者清空会话时，知道点原理还是有用的。
'''

# 创建引擎

''''
你应该已经写好了游戏地图和它的单元测试代码。现在我要求你制作一个简单的 游戏引擎，用来让游戏中的各个房间运转起来，从玩家收集输入，并且记住玩家 到了那一幕。我们将用到你刚学过的会话来制作一个简单的引擎，让它可以:
1. 为新用户启动新的游戏。 2. 将房间展示给用户。
3. 接受用户的输入。
4. 在游戏中处理用户的输入。
5. 显示游戏的结果，继续游戏的下一幕，知道玩家角色死亡为止。

为了创建这个引擎，你需要将我们久经考验的   搬过来，创建一个功 能完备的、基于会话的游戏引擎。这里的难点是我会先使用基本的 HTML 文件 创建一个非常简单的版本，接下来将由你完成它，基本的引擎是这个样子的:
'''
import web
from gothonweb import map

urls = (
'/game', 'GameEngine', 
'/', 'Index',
)

app = web.application(urls, globals())
# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions') 
	session = web.session.Session(app,store,initializer={'room': None})
	web.config._session = session
	
else:
	session = web.config._session
	render = web.template.render('templates/', base="layout")

class Index(object): 
	def GET(self):
			# this is used to "setup" the session with starting values
			session.room = map.START 
			web.seeother("/game")

class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room=session.room) 
		else:
			# why is there here? do you need it?
		return render.you_died()
		
	def POST(self):
		form = web.input(action=None)
		# there is a bug here, can you fix it?
		if session.room and form.action:
			session.room = session.room.go(form.action)
			
		web.seeother("/game")
		
if __name__ == "__main__":
	app.run()
	
'''
这个脚本里你可以看到更多的新东西，不过了不起的事情是，整个基于网页的游 戏引擎只要一个小文件就可以做到了。这段脚本里最有技术含量的事情就是将会 话带回来的那几行，这对于调试模式下的代码重载是必须的，否则每次你刷新网 页，会话就会消失，游戏也不会再继续了。
在你运行 bin/app.py 之前，你需要修改 PYTHONPATH 环境变量。不知道什 么是环境变量?为了运行一个最基本的 Python 程序，你就得学会环境变量， Python 的这一点确实有点挫。不过没办法，用 Python 的人就喜欢这样:
在你的命令行终端，输入下面的内容:
	export PYTHONPATH=$PYTHONPATH:.
如果你用的是 Windows，那就输入以下内容:

	set PYTHONPATH=%PYTHONPATH%;.

你只要针对每一个命令行会话界面输入一次就可以了，不过如果你运行 Python 代码时看到了 import 错误，那你就需要去执行一下上面的命令，或者也许是因 为你上次执行的 有错才导致 import 错误的。

 接下来你需要删掉 templates/hello_form.html 和 templates/index.html， 然后重新创建上面代码中 到的两个模板。这里是一个非常简单的 templates/show_room.html 供你参考:
	
$def with (room)
<h1> $room.name </h1>
<pre> $room.description </pre>
$if room.name == "death":
	<p><a href="/">Play Again?</a></p>
$else:
	<p>
	<form action="/game" method="POST">
		- <input type="text" name="action"> <input
	type="SUBMIT"> </form>
	</p>
	
 这就用来显示游戏中的房间的模板。接下来，你需要在用户跑到地图的边界时， 用一个 模板告诉用户他的角色的死亡信息，也就是 templates/you_died.html 这个模板:

<h1>You Died!</h1>
<p>Looks like you bit the dust.</p> 
<p><a href="/">Play Again</a></p>
	
	
准备好了这些文件，你现在可以做下面的事情了:
1. 让测试代码tests/app_tests.py再次运行起来，这样你就可以去测试这个游戏。 由于会话的存在，你可能顶多只能实现几次点击，不过你应该可以做出一些基本的 测试来。
2. 删除sessions/*下的文件，再重新运行一遍游戏，确认游戏是从一开始运行起 来的。
3. 执行pythonbin/app.py脚本，试玩一下你的游戏。
你需要和往常一样刷新和修正你的游戏，慢慢修改游戏的 HTML 文件和引擎，
直到你实现游戏需要的所有功能为止。

'''
#你的期末考试
'''
你有没有觉着我一下子给了你超多的信息呢?那就对了，我想要你在学习技能的 同时可以有一些可以用来鼓捣的东西。为了完成这节习题，我将给你最后一套需 要你自己完成的练习。你将注意到，到目前为止你写的游戏并不是很好，这只是 你的第一版代码而已。你现在的任务是让游戏更加完善，实现下面的这些功能:
'''

'''
1. 修正代码中所有我 到和没 到的 bug，如果你发现了新的 bug，你可以告诉我。
2. 改进所有的自动测试，让你可以测试更多的内容，直到你可以不用浏览器就能测到
所有的内容为止。
3. 让 HTML 页面看上去更美观一些。
4. 研究一下网页登录系统，为这个程序创建一个登录界面，这样人们就可以登录这个
   游戏，并且可以保存游戏高分。
5. 完成游戏地图，尽可能地把游戏做大，功能做全。
6. 给用户一个“帮助系统”，让他们可以查询每个房间里可以执行哪些命令。
7. 为你的游戏添加新功能，想到什么功能就添加什么功能。
8. 创建多个地图，让用户可以选择他们想要玩的一张来进行游戏。你
的 bin/app.py 应该可以运行 供给它的任意的地图，这样你的引擎就可以支持 多个不同的游戏。
9. 最后，使用你在习题 48 和 49中学到的东西来创建一个更好的输入处理器。你手 头已经有了大部分必要的代码，你只需要改进语法，让它和你的输入表单以及游戏 引擎挂钩即可。
祝你好运!
'''
#  下一步
'''
现在还不能说你是一个程序员。这本书的目的相当于给你一个“编程棕带”。你已 经了解了足够的编程基础，并且有能力阅读别的编程书籍了。读完这本书，你应 该已经掌握了一些学习的方法，并且具备了该有的学习态度，这样你在阅读其他 Python 书籍时也许会更顺利，而且能学到更多东西。
在 http://learnpythonthehardway.org/ 网站列出了一些你可以进一步阅读的免费 书籍，试着阅读它们，看看自己可以走多远。
或许，你现在已经可以开始鼓捣一些程序出来了。如果你手上有需要解决的问题， 试着写个程序解决一下。你一开始写的东西可能很挫，不过这没有关系。以我为 例，我在学每一种语言的初期都是很挫的。没有哪个初学者能写出完美的代码来， 如果有人告诉你他有这本事，那他只是在厚着脸皮撒谎而已。
最后，记住学习编程是要投入时间的，你可能需要至少每天晚上练习几个小时。 顺便告诉你，当你每晚学习 Python 的时候，我在努力学习弹吉他。我每天练 习 2 到 4 小时，而且还在学习基本的音阶。
每个人都是某一方面的菜鸟。
'''

#老程序员的建议		
'''

你已经完成了这本书而且打算继续编程。也许这会成为你的一门职业，也许你只 是作为业余爱好玩玩。无论如何，你都需要一些建议以保证你在正确的道路上继 续前行，并且让这项新的爱好为你带来最大程度的享受。
我从事编程已经太长时间，长到对我来说编程已经是非常乏味的事情了。我写这 本书的时候，已经懂得大约 20 种编程语言，而且可以在大约一天或者一个星 期内学会一门编程语言(取决于这门语言有多古怪)。现在对我来说编程这件事情
已经很无聊，已经谈不上什么兴趣了。当然这不是说编程本身是一件无聊的事情， 也不是说你以后也一定会这样觉得，这只是我个人在当前的感觉而已。
在这么久的旅程下来我的体会是:编程语言这东西并不重要，重要的是你用这些 语言做的事情。事实上我一直知道这一点，不过以前我会周期性地被各种编程语 言分神而忘记了这一点。现在我是永远不会忘记这一点了，你也不应该忘记这一 点。
你学到和用到的编程语言并不重要。不要被围绕某一种语言的宗教把你扯进去，
这只会让你忘掉了语言的真正目的，也就是作为你的工具来实现有趣的事情。
编程作为一项智力活动，是唯一一种能让你创建交互式艺术的艺术形式。你可以 创建项目让别人使用，而且你可以间接地和使用者沟通。没有其他的艺术形式能 做到如此程度的交互性。电影领着观众走向一个方向，绘画是不会动的。而代码 却是双向互动的。
编程作为一项职业只是一般般有趣而已。编程可能是一份好工作，但如果你想赚 更多的钱而且过得更快乐，你其实开一间快餐分店就可以了。你最好的选择是将 你的编程技术作为你其他职业的秘密武器。
技术公司里边会编程的人多到一毛钱一打，根本得不到什么尊敬。而在生物学、 医药学、政府部门、社会学、物理学、数学等行业领域从事编程的人就能得到足 够的尊敬，而且你可以使用这项技能在这些领域做出令人惊异的成就。
当然，所有的这些建议都是没啥意义的。如果你跟着这本书学习写软件而且觉得 很喜欢这件事情的话，那你完全可以将其当作一门职业去追求。你应该继续深入 拓展这个近五十年来极少有人探索过的奇异而美妙的智力工作领域。若能从中得 到乐趣当然就更好了。
最后我要说的是学习创造软件的过程会改变你而让你与众不同。不是说更好或更 坏，只是不同了。你也许会发现因为你会写软件而人们对你的态度有些怪异，也 许会用“怪人”这样的词来形容你。也许你会发现因为你会戳穿他们的逻辑漏洞而
他们开始讨厌和你争辩。甚至你可能会发现有人因为你懂得计算机怎么工作而觉 得你是个讨厌的怪人。
对于这些我只有一个建议: 让他们去死吧。这个世界需要更多的怪人，他们知道 东西是怎么工作的而且喜欢找到答案。当他们那样对你时，只要记住这是你的旅 程，不是他们的。“与众不同”不是谁的错，告诉你“与众不同是一种错”的人只是 嫉妒你掌握了他们做梦都不能想到的技能而已。
你会编程。他们不会。这真他妈的酷。
'''