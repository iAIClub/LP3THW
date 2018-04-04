# 习题12 提示别人
#y= raw_input("Name?")#在括号里可以放入提示的问题。用户输入就赋值给了y.
#  这里的意思是，习题11可以用更加简洁的方法表达出来。
''' 注意，这里发现，整整一段注释掉的话，用的是3个单引号，而不是在jianshu.com里面的三个【```】_键盘中1左上角的这个键。
age= raw_input("How old are you?")
height= raw_input("How tall are you?")
weight= raw_input("How much do you weight?")

print "So, you're %r old ,%r tall and %r heay."%(age,height,weight)
'''
# 上面被注释掉的一段在py2下测试通过。下面改成中文试试。

age= raw_input("您多大了？")
height= raw_input("你多高?")
weight= raw_input("你多重?")#中文字符可能出现问题，例如，如果本字符串如果携程“你有多种”则会出现乱码，所以尽量减少中文的使用。

print "所以，您的年龄是 %r ，高度是%r ，体重是 %r。"%(age,height,weight)# 在输入的时候，如果输入了中文也是会报错的，比如你需要输入的数字，你身高是175cm而不能输入175厘米，否则会报错。

''' #按照课后习题的加分题输入，报错，不知是怎么回事，回头再解决这个问题。
>>> pydoc raw_input
SyntaxError: invalid syntax
>>> python -m pydocraw_input
SyntaxError: invalid syntax
'''
