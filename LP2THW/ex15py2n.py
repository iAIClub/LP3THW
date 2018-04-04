from sys import argv #argv参数用于获取文件名变量。

script,filename=argv
#argv参数用于获取文件位置和文件名。带参数的变量。例如我可以在命令行里输入一个文件名（实际上需要用确切的地址和文件名）作为filename。这里其实是2个参数，第1个是脚本，

txt=open(filename)#注意open()命令类似raw_input()命令，接收一个参数，返回一个值。可以讲这个值赋予一个变量。这里，这个变量就是txt，被赋予了open（）函数的返回值。

print "Here's your file %r:"% filename #打印一个代占位and参量的字符串。

print txt.read()#我们在txt上 调用了一个函数。你从 open 获得的东西是一个file(文件)，文件本身也支持 一些命令。它接受命令的方式是使用句点.(英文称作 dot 或者 period)，紧跟 着你的命令，然后是类似 open 和 raw_input 一样的参数。不同点是:当你 说txt.read时，你的意思其实是:“嘿 txt!执行你的 read 命令，无需任何参 数!”

txt.close()
# close()# 新增加了一个关闭文件，先这样写着看看怎么样子？经过测试，我发现txt.close()是可以运行的，close()是无法运行的，无法正确运行。
print "GAME OVER"