# 第11题

print "Hello old are you?",#注意：这里语句的最后多了一个逗号（Comma）这样print就不会输出新行符号，而结束这一行跑到下一行了。
age= raw_input()#在py2里有raw_input（）函数，py3里没有，直接用input()
print "How tall are you?" #这个看看，如果语句后面没有Comma会发生什么状况？答案是：若果没加逗号的话，程序提示这个问题之后，接受用户输入需要另外起一行。加逗号的话，就是和这个问句的同一行。
height= raw_input()
print "How much do you weight?",
weight= raw_input()

print "So, you're %r old,%r tall and %r heavy." %(age,height,weight)#注意，这里前面的3个占位符分别和后面的3个变量相互配合。思考：为什么打印出来的时候age\weight\height, 上面都会使用单引号引用上呢？
# 运行完，并未见到例题中出现的【'6\'2"' 】而是【"6'22''" 】；另注意，当程序运行的时候输入【6'22''】这几个字是绿色的。和转义序列有关的，想想为什么最后一行 '6\'2"' 里边有一个 \' 序列。单引号需
#要被转义，从而防止它被识别为字符串的结尾。有没有注意到这一点？注意到了，但是，看样子还是单引号问题引起的混乱。我想如果转换了数据类型可能会好一些吧。
# LOG
# 20171023 从windows 端创建。
