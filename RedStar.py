# 绘制红色五角星
from turtle import *
fillcolor("yellow")
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

''' 为啥案例里是是新的红色五角星，我这里画出来的竟然是空心的五角星。'''
