# 将“字符串”赋值给"变量x"，该字符串中有个位置是用“%d”（包含格式）来代替的。%d这个符号看起来有两个作用：第一个作用是“占位符”——证明这个位置将来会有个东西放在这里；第二个作用是“这个东西的格式”，既然其使用了%d，我认为其应该是digital——数字的。

x= "There are %d types of people." %10

# 建立了给新的变量binary,将字符串“binary”赋值给了它。一般来说，变量会用简单的写法，竟然也可以直接使用单词。
binary="binary"
 
do_not="don't"
 
y="Those who know %s and those who %s."%(binary,do_not)#如果你想要在字符串中通过格式化字符放入多个变量的时候，你需要将变量放到（）圆括号里，变量之间采用逗号，隔开。
 
print x# print() 是个函数，必须有（），在2.0系列里print不用（）；x变量是字符串。

 
print y #y变量也是字符串。
 
print "I said: %r."% x# 我想的出来%d= digital %s=string 那么%r是什么鬼？百分号%确实是连续出现的，前面是格式，后面是变量（输入）。【例如 %r%r就是是非常有用的一个，它的含义是“不管什 么都打印出来”】
 
print "I also said:'%s'."%y#百分号%确实是连续出现的，前面是格式，后面是变量（输入）。
 
hilarious = False #hilarious 是欢闹的意思，这是个布尔变量，这里给他赋值 false。
 
joke_evaluation = "Isn't that joke so funny?! %r"#这里只有一个格式和占位符，没有变量输入？
 
print (joke_evaluation% hilarious)#第一个%前面是个字符窜变量，紧跟一个布尔变量是要做啥？
 
w="This is the left side of..." # 字符串1
 
e= "a string with a right side." # 字符串2
 
print w+e # 中间用+号 将两个字符串连接起来。
 
 
 # 只要将格式化的变量放到字符串中，再紧跟着一个百分号%，再紧跟着变量名即可。唯一要注意的地方，是如果你想要在字符串中通过格式化字符放入多个变量的时候，[你需要将变量放到（）圆括号里，变量之间采用逗号，隔开。]
 #试着使用更多的格式化字符，例如%s、%d、%r。例如 %r%r就是是非常有用的一个，它的含义是“不管什 么都打印出来”。
