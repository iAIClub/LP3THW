#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第26题 恭喜你，现在可以考试了!
##下面这是本节课的原文。
>'''
你已经差不多完成这本书的前半部分了，不过后半部分才是更有趣的。你将学到逻辑，并通过条件判断实现有用的功能。

在你继续学习之前，你有一道试题要做。这道试题很难，因为它需要你修正别人写的代码。当你成为程序员以后，你将需要经常面对别的程序员的代码，也许还 有他们的傲慢态度，他们会经常说自己的代码是完美的。

这样的程序员是自以为是不在乎别人的蠢货。优秀的科学家会对他们自己的工作持怀疑态度，同样，优秀的程序员也会认为自己的代码总有出错的可能，他们会先假设是自己的代码有问题，然后用排除法清查所有可能是自己有问题的地方，最后才会得出“这是别人的错误”这样的结论。在这节练习中，你将面对一个水平糟糕的程序员，并改好他的代码。

我将习题 24 和 25胡乱拷贝到了一个文件中，随机地删掉了一些字符，然后添加了一些错 误进去。大部分的错误是 Python在执行时会告诉你的，还有一些算术错误是你 要自己找出来的。再剩下来的就是格式和拼写错误了。

所有这些错误都是程序员很容易犯的，就算有经验的程序员也不例外。

【你的任务】是将此文件修改正确，用你所有的技能改进这个脚本。你可以先分析这个文件，或者你还可以把它像学期论文一样打印出来，修正里边的每一个缺陷，重复修正和运行的动作，直到这个脚本可以完美地运行起来。在整个过程中不要寻求帮助，如果你卡在某个地方无法进行下去，那就休息一会晚点再做。

就算你需要几天才能完成，也不要放弃，直到完全改对为止。 

最后要说的是，这个练习的目的不是写程序，而是修正现有的程序，你需要访问下面的网站: http://learnpythonthehardway.org/exercise26.txt从那里把代码复制粘贴过来，命名为ex26.py，这也是本书唯一一处允许你复制 粘贴的地方。
'''




##下面这个是粘贴来的代码原文：(修改前)



'''
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)

'''

## 下面这个是修改后的代码：

这里我不准备修改了，直接进入下一题。







# 运行后的结果：




