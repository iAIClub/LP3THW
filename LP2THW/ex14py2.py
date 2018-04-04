# 第14题
# 使用argv和raw_input 一起来向用户提特别的问题。这是下一节习题读写的基础。
#说实话，后面这句话我没看懂——{我们将用户提示符设置为变量 prompt，这样我们就不需要在每次用到 raw_input 时重复输入提示用户的字符了。而且如果你要将提示符修改成别的字串，你只要改一个位置就可以了}

from sys import argv #引入了一个argv

script , user_name = argv #这个argv有2个参量：script（程序名称）user_name（用户名）

prompt='>' # 引入一个新变量prompt 用来代表＞号。

print "Hi %s, I'm the %s script." %(user_name,script)#将两个参量分别引入字符串句子中。

print "I'd like to ask you a few questions."

print "Do you like me %s?"%user_name#引入用户输入参量1

likes= raw_input(prompt)# 将prompt作为参量再次作为input输入，赋值给likes这个变量。

print "Where do you live %s?"% user_name

lives=raw_input(prompt)# 将prompt作为参量再次作为input输入，赋值给lives这个变量。

print "What kind of computer do you have?"

computer=raw_input(prompt) #将prompt这个变量赋值给变量computer

print"""
Alright,so you said %r about liking me.# 这里的占位符后面没有跟变量。

You live in %r. Not sure where that is.# 占位符后面没有跟变量，而且is被提示了，说明is是一个专业名字，但是在这里估计是没啥鸟用。

And you have a %r computer. Nice.# 这里也有一个占位符，估计也没啥用。

"""% (likes,lives,computer) #在Python自带IDE中这行被涂成绿色，意思是注释掉了，但是这行还是有用的语句。
# 我明白了，在两个{三个双引号""" }之间理论上被注释或者成段打印的多段字符串，里面的站位符，可以被最后的三引号之外的参数，集中引用。
# 注意连续的三个半角的双引号之间不可以有空格，最后的三个双引号也是如此。

### 以下是运行的结果
'''
PS C:\Users\Administrator> python E:\AllFilesIo\PythonIO\Python_LP2THW\ex14py2.py Andy
Hi Andy, I'm the E:\AllFilesIo\PythonIO\Python_LP2THW\ex14py2.py script.
I'd like to ask you a few questions.
Do you like me Andy?
>Yes
Where do you live Andy?
>Tianjin
What kind of computer do you have?
>ThinkPad

Alright,so you said 'Yes' about liking me.# 杩欓噷鐨勫崰浣嶇鍚庨潰娌℃湁璺熷彉閲忋€?

You live in 'Tianjin'. Not sure where that is.# 鍗犱綅绗﹀悗闈㈡病鏈夎窡鍙橀噺锛岃€屼笖is琚彁绀轰簡锛岃鏄巌s鏄竴涓
笓涓氬悕瀛楋紝浣嗘槸鍦ㄨ繖閲屼及璁℃槸娌″暐楦熺敤銆?

And you have a 'ThinkPad' computer. Nice.# 杩欓噷涔熸湁涓€涓崰浣嶇锛屼及璁′篃娌″暐鐢ㄣ€?
'''
# 以下内容是在macbook中运行的结果
''''

itifadeMacBook-Pro:~ yyy$ python /Users/yyy/Documents/Python_LP2THW/ex14py2.py Andy
Hi Andy, I'm the /Users/yyy/Documents/Python_LP2THW/ex14py2.py script.
I'd like to ask you a few questions.
Do you like me Andy?
>No
Where do you live Andy?
>China
What kind of computer do you have?
>Macbook

Alright,so you said 'No' about liking me.# 这里的占位符后面没有跟变量。

You live in 'China'. Not sure where that is.# 占位符后面没有跟变量，而且is被提示了，说明is是一个专业名字，但是在这里估计是没啥鸟用。

And you have a 'Macbook' computer. Nice.# 这里也有一个占位符，估计也没啥用。


itifadeMacBook-Pro:~ yyy$ 
'''