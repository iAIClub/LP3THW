from sys import argv #argv参数用于获取文件名变量。

script,filename=argv #argv参数用于获取文件位置和文件名。带参数的变量。例如我可以在命令行里输入一个文件名（实际上需要用确切的地址和文件名）作为filename。这里其实是2个参数，第1个是脚本，

txt= open(filename)#注意open()命令类似raw_input()命令，接收一个参数，返回一个值。可以讲这个值赋予一个变量。这里，这个变量就是txt，被赋予了open（）函数的返回值。

print "Here's your file %r:"% filename #打印一个代占位and参量的字符串。

print txt.read()#我们在txt上 调用了一个函数。你从 open 获得的东西是一个file(文件)，文件本身也支持 一些命令。它接受命令的方式是使用句点.(英文称作 dot 或者 period)，紧跟 着你的命令，然后是类似 open 和 raw_input 一样的参数。不同点是:当你 说txt.read时，你的意思其实是:“嘿 txt!执行你的 read 命令，无需任何参 数!”

# 思考，上面这种读取文件名的方法好，还是下面这种方法好？为啥？

print "Type the filename again:"# 这里要求再次输入filename，其实是包含被打开的文件名称在内的整个完整路径。

file_again= raw_input(">")# 注意：raw_input()命令，这里，我理解使用file_again这个变量获得字符串“>”这个参量。

txt_again= open(file_again)#open()函数后面接了一个变量file_again,也就是字符串“>”，有什么用呢？明白了，这里在使用者看来，只需要在>后面输入内容就行了，当然输入的这些内容(希望被导入的文件名称)实际上被赋给了file_again这个参量，然后又通过open（）函数赋值给了 txt_again这个参量。

print txt_again.read()#txt_again这个参量，竟然会有read()方法——相当于说：Hey，字符串参量txt_again你去执行你的read命令，无需参数。

''''
运行后显示的结果：注意，提到的文件和路径必须完整才行。

itifadeMacBook-Pro:~ yyy$ python  Documents/Python_LP2THW/ex15py2.py Documents/Python_LP2THW/ex15py2_sample.txt
Here's your file 'Documents/Python_LP2THW/ex15py2_sample.txt':
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have i here.
Type the filename again:
>Documents/Python_LP2THW/ex15py2_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have i here.
itifadeMacBook-Pro:~ yyy$ 

'''
# 由于安装路径的问题，现在用python经常用到路径，还是比较别手的。有点烦躁。折腾一早上，完成1题，还不算加分部分（本章很重要，作者要求你做好加分题）




''''
现在请在命令行运行 pydoc open 来读读它的说 明。
在mac中可以清晰的看到和使用pydoc 这个命令
itifadeMacBook-Pro:~ yyy$ pydoc open

Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.
(END)
'''
# The Code Below can be Use,testig passed.
'''
from sys import argv #argv参数用于获取文件名变量。

script,filename=argv
#argv参数用于获取文件位置和文件名。带参数的变量。例如我可以在命令行里输入一个文件名（实际上需要用确切的地址和文件名）作为filename。这里其实是2个参数，第1个是脚本，

txt=open(filename)#注意open()命令类似raw_input()命令，接收一个参数，返回一个值。可以讲这个值赋予一个变量。这里，这个变量就是txt，被赋予了open（）函数的返回值。

print "Here's your file %r:"% filename #打印一个代占位and参量的字符串。

print txt.read()#我们在txt上 调用了一个函数。你从 open 获得的东西是一个file(文件)，文件本身也支持 一些命令。它接受命令的方式是使用句点.(英文称作 dot 或者 period)，紧跟 着你的命令，然后是类似 open 和 raw_input 一样的参数。不同点是:当你 说txt.read时，你的意思其实是:“嘿 txt!执行你的 read 命令，无需任何参 数!”

----
# It Can be Seen From The Terminal,like this:
itifadeMacBook-Pro:~ yyy$ python  Documents/Python_LP2THW/ex15py2n.py Documents/Python_LP2THW/ex15py2_sample.txt
Here's your file 'Documents/Python_LP2THW/ex15py2_sample.txt':
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have i here.
itifadeMacBook-Pro:~ yyy$ 

'''
