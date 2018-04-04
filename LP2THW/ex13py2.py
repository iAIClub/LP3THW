# 习题13：参数(argument)、解包、变量

from sys import argv# import 是引入功能

script,first,second,third = argv
#argv 是所谓参数变量(argument variable)这个变量包含了你传递给Python的参数
# 上面这一行是解包，将其所有参数放到同一个变量下面，我们将每个参量赋予一个变量名：scipt~first~。所谓解开包的意思是：把argv中的东西解包，将所有参数依次赋予左边的变量名中。
# 其实import导入的是一个模组（modules）或者叫做库（libraries）,意思是你要把sys模组（库）inport进来。

print "The scipt is called:",script # script这个参数其实是某一个路径下的一个文件。

print "Your first variable is:",first

print"Your second variable is:",second

print  "Your third variable is:",third

'''
# ！！重要发现，由于一直没搞清楚命令行怎么运行Python程序，而这里又设计到带参数的Python运行，所以这里一直错误。
# ！现在我将讲讲错在哪里，并且怎么解决的。教材中说，只需要python ex13.py first 2nd 3rd(后面这三个是参数)
# 但是我一直也调用不出来。关键是命令行怎么调用这个程序就搞不清。
#好吧，在windows 运行下输入powershell （貌似直接输入python 也可以调用出来c:\python27\python.exe）， 然后出现了命令行窗口（很丑，搞不清楚他们为啥要用），
#  在powershell里直接输入python进入了python2.7 然后输入ex13py2.py没反应,ex13py2.py报错。想办法返回上一级。
#  直接在python界面里是无法带参数运行这个.py程序的。现在需要的是点Ctrl+Z返回到上一层，对于我来说也就是
# 也就是路径“PS C:\Users\Administrator>”
# 用自带的IDLE打开你编写的这个py文件，里面有个路径，对于我来说是E:\AllFilesIo\PythonIO\Python_LP2THW\ex13py2.py
# 然后我在上面这个路径下面输入：python E:\AllFilesIo\PythonIO\Python_LP2THW\ex13py2.py first 2nd 3rd  #py文件后面紧跟着的3个就是参数，这样就能调试通过了。
# 总结：直接在IDLE里面编辑的py文件，如果需要通过命令行+参数的方法运行，需要在powershell里通过ctrl+Z进入到上一级路径，在这个基础上 输入[python  路径  参数1 参数2 参数3]回车运行。
#和其他编辑器不同（ctrl+v），在powershell窗口里面，粘贴只需要右键就行可以了。（这个路径是通过Python自带的IDE运行之后，上面标注的路径，才copy出来的。）
'''
'''
运行后显示如下：这里用了cheese apple bread共3个参数。
PS C:\Users\Administrator> python E:\AllFilesIo\PythonIO\Python_LP2THW\ex13py2.py cheese apple bread
The scipt is called: E:\AllFilesIo\PythonIO\Python_LP2THW\ex13py2.py
Your first variable is: cheese
Your second variable is: apple
Your third variable is: bread
PS C:\Users\Administrator>

'''

# 如果 多填写了一个，就会出现如下状况
'''
PS C:\Users\Administrator> python E:\AllFilesIo\PythonIO\Python_LP2THW\ex13py2.py cheese apple bread blue
Traceback (most recent call last):
  File "E:\AllFilesIo\PythonIO\Python_LP2THW\ex13py2.py", line 5, in <module>
    script,first,second,third = argv
ValueError: too many values to unpack
PS C:\Users\Administrator>
'''
# 加分题【将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入】我没做，因为不知道如何将raw_input作为参数来使用。

