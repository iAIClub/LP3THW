#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第49题 创建句子
# 以下是代码部分
## 从我们这个小游戏的词汇扫 器中，我们应该可以得到类似下面的列表:
>>> from ex48 import lexicon
>>> print lexicon.scan("go north")
[('verb','go'),('direction','north')]
>>> print lexicon.scan("kill the princess")
[('verb','kill'),('stop','the'),('noun','bear')]
>>> print lexicon.scan("open the door and smack the bear in the nose")
[('error','open'),('stop','the'),('noun','door'),('error','and'),('error', 'smack'), ('stop', 'the'), ('noun', 'bear'), ('stop', 'in'),
('stop', 'the'), ('error', 'nose')]
>>>

# 现在让我们把它转化成游戏可以使用的东西，也就是一个Sentence类。我们的目的是将上面的元组列表转换为一个Sentence对象，而这个对象又保安主谓宾各个成员。

## 匹配（Match）和窥视（Peek）
'''
为了达到这个效果，你需要四样工具:
1. 循环访问元组列表的方法，这挺简单的。
2. 匹配我们的主谓宾设置中不同种类元组的方法。
3. 一个“窥视”潜在元组的方法，以便做决定时用到。
4. 跳过(skip)我们不在乎的内容的方法，例如形容词、冠词等没有用处的词汇。
 我们使用 peek 函数来查看元组列表中的下一个成员，做匹配以后再对它做下 一步动作。让我们先看看这个 peek 函数
'''
## peek()函数
def peek(word_list):
	if word_list:
		word =word_list[0]
		return word[0]
	else:
		return None
		
# match()函数：
def match(word_list,expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0]== expectiong:
			return word
		else:
			return None
	else:
		return None
		
#skip()函数

def skip(word_list,word_type):
	while peek(word_list)== word_type:
		match(word_list,word_type)
		
# 句子的语法：
'''
有了工具，我们现在可以从元组列表来构建句子（sentence）对象了，我们的处理流程如下：
1.使用peek识别下一个单词。
2.如果这个单词和我们的语法匹配，我们就调用一个函数来处理这部分语法。假设函数的名称叫做parse_subject好了。
3.如果语法不匹配，我们就raise 一个错误，接下来你会学到这个方面的内容。
4.全部分析完以后，我们应该能得到一个　Sentence对象，然后可以将其应用在我们的游戏中。

演示这个过程最简单的方法是把代码韩式给你让你阅读，不过这节习题有个不一样的要求，前面是我给你测试代码，你照着写出程序来，而这次是我给你的程序，你要为他写出测试代码来。
以下就是我写的用来解析简单句子的代码，它使用了ex48.lexicon这个模组。
'''
class ParserError(Exception):
	pass
	
	
class Sentence(object):
	
	def _init_(self,subject,verb,object):
		# remember we take('noun','princess')tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
		
def peek(word_list):
	if word_list:
		word =word_list[0]
		return word[0]
	else:
		return None
		
def match(word_list,expecting):
	if word_list:
		word =word_list.pop(0)
		
		if word[0]== expecting:
			return word
		else:
			return None
	else:
		return None
		
def skip(word_list,word_type):
	while peek(word_list)== word_type:
		match(word_list,word_type)
		
def parse_verb(word_list):
	skip(word_list,'stop')
	
	if peek(word_list)=='verb':
		return match(word_list,'verb')
	else:
		raise ParserError(''Expected a verb next.'')
		
def parse_object(word_list):
	skip(word_list,'stop')
	next = peek(word_list)
	
	if next == 'noun':
		return match(word_list,'noun')
	if next == 'direction':
		return match(word_list,'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		
def parse_subject(word_list,subj):
	verb = parse_verb(word_list)
	obj =parse_object(word_list)
	
	return Sentence (subje,verb,obj)

def parse_sentence(word_list):
	skip(word_list,'stop')
	
	start = peek(word_list)
	
	if start =='noun':
		subj = match(word_list,'noun')
		return parse_subject(word_list,subj)
	elif start == 'verb':
		# assume the subject is the player then
		return parse_subject(word_list,('noun','player'))
	else:
		raise ParserError ("Must start with subject,object,or verb not: %s" % start)
		
# 关于异常(Exception)
'''
你已经简单学过关于异常的一些东西，但还没学过怎样抛出(raise)它们。这节的 代码演示了如何 raise 前面定义的ParserError。注意   是一个定 义为Exception类型的 class。另外要注意我们是怎样使用   这个关键字 来抛出异常的。
你的测试代码应该也要测试到这些异常，这个我也会演示给你如何实现。
'''
# 你应该测试的东西
'''
为《习题 49》写一个完整的测试方案，确认代码中所有的东西都能正常工作， 其中异常的测试——输入一个错误的句子它会抛出一个异常来。
使用assert_raises这个函数来检查异常，在 nose 的文档里查看相关的内容， 学着使用它写针对“执行失败”的测试，这也是测试很重要的一个方面。从 nose 文档中学会使用 assert_raises，以及一些别的函数。
写完测试以后，你应该就明白了这段程序的工作原理，而且也学会了如何为别人 的程序写测试代码。 相信我，这是一个非常有用的技能。
'''
## 加分习题
'''
1. 修改parse_函数(方法)，将它们放到一个类里边，而不仅仅是独立的方法函数。 这两种程序设计你喜欢哪一种呢?
2.  高 parser 对于错误输入的抵御能力，这样即使用户输入了你预定义语汇之外的
词语，你的程序也能正常运行下去。
3. 改进语法，让它可以处理更多的东西，例如数字。
4. 想想在游戏里你的 Sentence 类可以对用户输入做哪些有趣的事情。
'''
	


# 运行后的结果：
'''
本题就是照着敲了代码，并没有进行进一步的测试和运行。
'''


