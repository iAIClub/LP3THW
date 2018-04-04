#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第50题 -你的第一个网站
 
# 以下是代码部分
'''
这节以及后面的习题中，你的任务是把前面创建的游戏做成网页版。这是本书的 最后三个章节，这些内容对你来说难度会相当大，你要在上面花些时间才能做出 来。在你开始这节练习以前，你必须已经成功地完成过了《习题 46》的内容， 正确安装了 pip，而且学会了如何安装软件包以及如何创建项目骨架。如果你不 记得这些内容，就回到《习题 46》重新复习一遍。
'''
# 安装lpthw.web
'''
在创建你的第一个网页应用程序之前，你需要安装一个“Web 框架”，它的名字 叫 lpthw.web。所谓的“框架”通常是指“让某件事情做起来更容易的软件包”。在 网页应用的世界里，人们创建了各种各样的“网页框架”，用来解决他们在创建网 站时碰到的问题，然后把这些解决方案用软件包的方式发布出来，这样你就可以 利用它们引导创建你自己的项目了。
可选的框架类型有很多很多，不过在这里我们将使用   框架。你可以 先学会它，等到差不多的时候再去接触其它的框架，不过   本身挺不 错的，所以就算你一直使用也没关系。

'''
## 使用pip安装 lpthw.web:
'''
## 出现提示：
Last login: Mon Nov  6 10:49:31 on console
itifadeMacBook-Pro:~ yyy$ sudo pip install lpthw.web
Password:
The directory '/Users/yyy/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/yyy/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting lpthw.web
  Downloading lpthw.web-1.1.tar.gz (87kB)
    100% |████████████████████████████████| 92kB 650kB/s 
Installing collected packages: lpthw.web
  Running setup.py install for lpthw.web ... done
Successfully installed lpthw.web-1.1
itifadeMacBook-Pro:~ yyy$ 


'''
##  由于我的安装不是在根目录里，所以经常会遇到上面的权限不足的问题。itifa当时告诉我，更换了账户后登陆“终端”可能会遇到一些问题，现在果然遇到问题了，就是所谓权限不足的问题。
## 解决方案1：
## 解决方案2:直接进入itifa账户然后将这个账户改名。把原来的文件重新 copy到初始账户里。

## 上面这个问题的解决方案参见
'''
源自：http://blog.sina.com.cn/s/blog_a046022d0102w2ux.html

（1）使用命令：sudo pip install numpy时，可能遇到：
The directory '/Users/huangqizhi/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
说得很清楚，是pip目录的属主不是sudo的root用户。如果必须用sudo pip，更改pip目录属主即可：
sudo chown root /Users/huangqizhi/Library/Caches/pip

（2）pip安装时，可能遇到：
/Library/Python/2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
解决方法：安装requests，注意后面带[security]：
pip install requests[security]

'''
# 这个地方的氛围已经相当的压抑了
'''

然后使用下面的方法来运行这个 web 程序:
 
$ python bin/app.py
http://0.0.0.0:8080/
 
最后，使用你的网页浏览器，打开 URL ，你应该看 到两样东西，首先是浏览器里显示了   ，然后是你的命令行终端 显示了如下的输出:
http://localhost:8080/
Hello, world!
$ python bin/app.py http://0.0.0.0:8080/
127.0.0.1:59542 - - [13/Jun/2011 11:44:43] "HTTP/1.1 GET /" - 200 OK
127.0.0.1:59542 - - [13/Jun/2011 11:44:43] "HTTP/1.1 GET /favicon.ico" - 404 Not Found
这些是lpthw.web打印出的 log 信息，从这些信息你可以看出服务器有在运行， 而且能了解到程序在浏览器背后做了些什么事情。这些信息还有助于你发现程序
的问题。例如在最后一行它告诉你浏览器试图获取 /favicon.ico，但是这个文 件并不存在，因此它返回的状态码是 404 Not Found。
到这里，我还没有讲到任何 web 相关的工作原理，因为首先你需要完成准备工 作，以便后面的学习能顺利进行，接下来的两节习题中会有详细的解释。我会要 求你用各种方法把你的 lpthw.web 应用程序弄坏，然后再将其重新构建起来: 这样做的目的是让你明白运行 lpthw.web 程序需要准备好哪些东西。
'''

## 发生了什么事情？
'''
在浏览器访问到你的网页应用程序时，发生了下面一些事情:
 
1. 浏览器通过网络连接到你自己的电脑，它的名字叫做localhost，这是一个标准 称谓，表示的谁就是网络中你自己的这台计算机，不管它实际名字是什么，你都可 以使用 localhost 来访问。它使用到的网络端口是 5000。
2. 连接成功以后，浏览器对bin/app.py这个应用程序发出了 HTTP 请求(request)， 要求访问 URL/，这通常是一个网站的第一个 URL。
3. 在bin/app.py里，我们有一个列表，里边包含了 URL 和类的匹配关系。我们 这里只定义了一组匹配，那就是 '/', 'index' 的匹配。它的含义是:如果有人 使用浏览器访问 / 这一级目录，lpthw.web 将找到并加载 class index，从而 用它处理这个浏览器请求。
4. 现在lpthw.web找到了classindex，然后针对这个类的一个实例调用 了 index.GET 这个方法函数。该函数运行后返回了一个字符串，以供 lpthw.web 将其传递给浏览器。
5. 最后lpthw.web完成了对于浏览器请求的处理，将响应(response)回传给浏览器， 于是你就看到了现在的页面。
 
 
确定你真的弄懂了这些，你需要画一个示意图，来理清信息是如何从浏览器传递 到 lpthw.web，再到 index.GET，再回到你的浏览器的。
'''
## 修正错误
'''
第一步，把第 11 行的greeting变量赋值删掉，然后刷新浏览器。你应该会看 到一个错误页面，你可以通过这一页丰富的错误信息看出你的程序崩溃的原因是 什么。当然你已经知道出错的原因是 greeting 的赋值丢失了，不
过 lpthw.web 还是会给你一个挺好的错误页面，让你能找到出错的具体位置。 试试在这个错误页面上做以下操作:
1. 检查每一段Localvars输出(用鼠标点击它们)，追踪里边 到的变量名称，以 及它们是在哪些代码文件中用到的。
2. 阅读RequestInformation一节，看看里边哪些知识是你已经熟悉了的。 Request 是浏览器发给你的gothonweb应用程序的信息。这些知识对于日常网页 浏览没有什么用处，但现在你要学会这些东西，以便写出 web 应用程序来。
3. 试着把这个小程序的别的位置改错，探索一下会发生什么事情。``lpthw.web`` 的会 把一些错误信息和堆栈跟踪(stack trace)信息显示在命令行终端，所以别忘了检查命 令行终端的信息输出。
'''
##  创建基本的模版文件
'''
你已经试过用各种方法把这个 lpthw.web 程序改错，不过你有没有注意到“Hello World”不是一个好 HTML 网页呢?这是一个 web 应用，所以需要一个合适的 HTML 响应页面才对。为了达到这个目的，下一步你要做的是将“Hello World” 以较大的绿色字体显示出来。
第一步是创建一个   文件，内容如下:
templates/index.html
'''
#以下是HTML代码
'''
$def with (greeting)

<html>
	<head>
		<title>Gothons Of Planet Percal #25</title>
		
	</head>
<body>
	
$if greeting:
	I just wanted to say <em style ="color:green;font-size:2em;">$greeting</em>.
$else:
	<em>Hello</em>,world!
</body>
</html>
'''
# 代码
'''
如果你学过 HTML 的话，这些内容你看上去应该很熟悉。如果你没学过 HTML， 那你应该去研究一下，试着用 HTML 写几个网页，从而知道它的工作原理。不 过我们这里的 HTML 文件其实是一个“模板(template)”，如果你向模板 供一些 参数，lpthw.web 就会在模板中找到对应的位置，将参数的内容填充到模板中。 例如每一个出现 $greeting 的位置，$greeting 的内容都会被替换成对应这个变量名的参数。
为了让你的 bin/app.py 处理模板，你需要写一写代码，告诉 lpthw.web 到哪 里去找到模板进行加载，以及如何渲染(render)这个模板，按下面的方式修改你 的 app.py:
'''
'''
特别注意render这个新变量名，注意我修改了index.GET的最后一行，让它返回了render.index()，并且将greeting变量作为参数传递给了这个函数。
改好上面的代码后，刷新一下浏览器网页妞就会看到一条和之间不同风绿色信息输出。你还可以在六拉起中查看源文件（View Source）,看到模版被渲染成了标准有效的HTML源码。
	1. 在bin/app.py里面你添加了一个叫做render的新变量，它本身是一 个 web.template.render 对象。
	2. 你将templates/作为参数传递给了这个对象，这样就让render知道了从哪里 去加载模板文件。
	3. 在你后面的代码中，当浏览器一如既往地触发了index.GET以后，它没有再返回 简单的 greeting 字符串，取而代之的是你调用了 render.index，而且将问候 语句作为一个变量传递给它。
	4. 这个render_template函数可以说是一个“魔法函数”，它看到了你需要的
	是 index.html，于是就跑到 templates/ 目录下，找到名字为 index.html 的 文件，然后就把它渲染(render)一遍(叫“转换一遍”也可以)。
	5. 在templates/index.html文件中，你可以看到初始定义一行中说这个模板需 要使用一个叫greeting的参数，这和函数定义中的格式差不多。另外和 Python 语法一样，模板文件是缩进敏感的，所以要确认自己弄对了缩进。
	6. 最后，你让templates/index.html去检查greeting这个变量，如果这个变
	量存在的话，就打印出变量的内容，如果不存在的话，就会打印出一个默认的问候 信息。
	
	要深入理解这个过程，你可以修改 greeting 变量以及 HTML 模板的内容，看 看会有什么效果。然后创建一个叫做 templates/foo.html 的模板，并且使用 一个新的 render.foo 去渲染它。从这个过程你也可以看出，render 调用的函 数名称只要跟templates/下的.html文件名匹配到，这个 HTML 模板就可以 被渲染到了。
	
#加分题
加分习题1. 到http://webpy.org/阅读里边的文档，它其实和     是同一个项目。lpthw.web198
 2. 实验一下你在上述网站看到的所有的东西，包括里边的代码示例。3. 阅读以下 HTML5 和 CSS3 相关的东西，自己练习着写几个 .html 和 .css 文件。 4. 如果你有一个懂 Django 朋友可以帮你的话，你可以试着使用 Django 完成一下习题 50、51、52，看看结果会是什么样子的。






# 运行后的结果：
'''

'''


