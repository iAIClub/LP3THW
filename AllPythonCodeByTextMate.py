#TempConvert.py
val = input ("请输入带温度表示符号的温度值，（例如：32C）：")
if val[-1] in ['C','c']:
    f= 1.8 * float(val[0:-1])+32
    print ("转换后的温度为：%.2fF"%f)
elif val[-1] in ['F','f']:
    c=(float(val[0:-1])-32)/1.8
    print ("转换后的温度为：%.2fC"%c)
else:
    print("输入有误")

# Chap1_1WordIsBig字符拼接
str1 = input("请输入一个人的名字：")
str2 = input("请输入一个国家名字：")
print ("世界那么大，{}想去{}看看。".format(str1,str2))
'''测试通过

于小焱  意大利'''


#chp1_IntSum_整数序列求和
n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum +=  i    +   1
print ("1到N求和结果：",sum)
#chp1_9*9_九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print ("{}*{}={:2}".format(j,i,i*j),end='')
    print('')


# 阶乘计算
sum, tmp =  0, 1
for i in range(1,11):
    tmp*=i
    sum+=tmp

print ("运算结果是：{}".format(sum))

#--
#

# 绘制红色五角星
from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()
''' 为啥案例里是是新的红色五角星，我这里画出来的竟然是空心的red五角星。'''
# Beautiful graphic blue
from turtle import *
fillcolor("blue")
begin_fill()
while True:
    forward(400)
    right(244)
    if abs(pos()) < 1:
        break
end_fill()

''' 上面划出一个非常漂亮的蓝色图案，简直是美呆了。'''

# (8)太阳花

from turtle import *
color ('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
'''这个程序可以运行，就是不清楚为啥案例填充全是黄色，而我的中间还有个白心。'''

#(9)螺旋线绘制
import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)
'''这个程序可以完美运行,range(100)处100可以改成其他的200-300，结果不一样'''

#（10）彩色螺旋线
import turtle
import time
turtle.pensize(2)
turtle.bgcolor('black')
colors=["red","yellow",'purple',"blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
turtle.tracer(True)
'''亲测可用'''

#(11)猴子吃桃子
n= 1
for i in range (5,0,-1):
    n=(n+1)<<1
print(n)
'''94啦，可以算出来，但是，我总是会忘记表达式for一行中的：'''

#(12)物种饮食
diet = ['西红柿',   '花椰菜',  '黄瓜',   '牛排',    '虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))

# 蟒蛇
import turtle
