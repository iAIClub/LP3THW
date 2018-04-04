#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第46题 一个项目骨架
# 以下是代码部分
'''
这里你将学会如何建立一个项目“骨架”目录。这个骨架目录具备让项目跑起来的所有基本内容。它里边会包含你的项目文件布局、自动化测试代码，模组，以及安装脚本。当你建立一个新项目的时候，只要把这个目录复制过去，改改目录的名字，再编辑里边的文件就行了。
'''
## 骨架内容
### 首先使用下述命令创建你的骨架目录：
'''
~ $ mkdir -p projects
~ $ cd projects/
~/projects $ mkdir skleton
~/projects $ cd skeleton
~/projects/skeleton $ mkdir in NAME tests docs
'''
### 我使用了一个叫做projects 的目录来存放我自己的各个项目。然后我在李彬啊建立了一个叫做 skeleton 的文件夹，这就是我们新项目的基础目录。其中叫做NAME的文件夹是你的项目等主要文件夹，你剋一将它任意明明。

##接下来我们要配置一些初始文件：

'''
~/projects/skeleton $ touch NAME/_init_.py
~/projects/skeleton $ touch tests/_init_.py


'''
## 以上命令为你创建了空的模组目录，以供你后面为其添加代码。然后我们需要建立一个setup.py文件，这个文件在安装项目的时候我们会用到它。

## 文件名  setup.py
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config ={
	'description':'My Project',
	'author':'My Name',
	'url':'URL to ger it at.',
	'download_url':'Where to download it.',
	'author_email':'My email.',
	'version':'0.1',
	'install_requires':['nose'],
	'packeage':['NAME'],
	'scripts':[],
	'name':'projectname'
}

setup(**config)

#编辑这个文件，把自己的练习方式写进去，然后放到那里就行了。最后你需要一个简单的测试专用的骨架文件叫tests/NAME_tests.py



## 文件名NAME_tests.py
from nose.tools import *
import NAME

def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"
	
def test_basic():
	print "I RAN!"
	
## Python 软件包的安装
''''
接下来你需要安装下面的软件包:
1. pip – http://pypi.python.org/pypi/pip
2. distribute – http://pypi.python.org/pypi/distribute
3. nose – http://pypi.python.org/pypi/nose/
4. virtualenv – http://pypi.python.org/pypi/virtualenv



我要预先警告你，这个过程会是相当无趣。在业内我们将这种事情叫做 “yak shaving(剃牦牛)”。它指的是在你做一件有意义的事情之前的一些准备工作，而这些准备工作又是及其无聊冗繁的。你要做一个很酷的 Python 项目，但是创建骨架目录需要你安装一些软件包，而安装软件包之前你还要安装 package installer(软件包安装工具)，而要安装这个工具你还得先学会如何在你的操作系统下安装软件，真是烦不胜烦呀。无论如何，还是克服困难把。你就把它当做进入编程俱乐部的一个考验。每个程序员都会经历这条道路，在每一段“酷”的背后总会有一段“烦”的。
'''
##测试你的配置
'''
安装了所有上面的软件包以后，你就可以做下面的事情了:
~/projects/skeleton $ nosetests .
-------------------------------------------------------- --------------
Ran 1 test in 0.007s
OK
 
下一节练习中我会告诉你 nosetests 的功能，不过如果你没有看到上面的画面， 那就说明你哪里出错了。确认一下你的NAME和tests目录下存在__init__.py， 并且你没有把 tests/NAME_tests.py 命名错。

'''
##使用这个骨架
'''
剃牦牛的事情已经做的差不多了，以后每次你要新建一个项目时，只要做下面的 事情就可以了:
1. 拷贝这份骨架目录，把名字改成你新项目的名字。
2. 再将 NAME 模组更名为你需要的名字，它可以是你项目的名字，当然别的名字也
行。
3. 编辑 setup.py 让它包含你新项目的相关信息。
4. 重命名tests/NAME_tests.py，让它的名字匹配到你模组的名字。
5. 使用nosetests检查有无错误。
6. 开始写代码吧。

'''
## 小测验
'''
小测验
这节练习没有加分习题，不过需要你做一个小测验:
1. 找文档阅读，学会使用你前面安装了的软件包。
2. 阅读关于setup.py的文档，看它里边可以做多少配置。Python 的安装器并不是一个好软件，所以使用起来也非常奇怪。
3.创建一个项目，在模组目录里写一些代码，并让这个模组可以运行。
4.在目录下放一个可以运行的脚本，找材料学习一下怎样创建可以在系统下运行bin的 Python 脚本。
5.在你的setup.py中加入bin这个目录，这样你安装时就可以连它安装进去。 
6.使用setup.py安装你的模组，并确定安装的模组可以正常使用，最后使用pip将其卸载。
'''


# 运行后的结果：
'''
本章学的云里雾里。大概是说要在网上有这种模块可以自动安装一些“包”和“模块”
'''


