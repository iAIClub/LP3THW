import easygui as g
import sys

'''
#gui编程中常见的一个场景是要求用户输入目录或者文件名
#easygui提供了一些基本的函数让用户来浏览文件系统,选择一个目录或者文件.
str1=g.diropenbox('选择文件目录','浏览文件夹','C:/Users/Administrator/Desktop')
g.msgbox(str1)
'''

while 1:
    g.msgbox("显示一个窗口并且显示这些文字")# 只显示一个对话框并且只有一个ok
    msg="你希望学到什么呢?"
    title="小游戏互动"       # 在左上角的 标题旷里面
    choices=['谈恋爱','编程','ooxx','琴棋书画']  # 在选择框内 , 提供可选择项
    choice=g.choicebox(msg,title,choices) #  在这里 choice 可以得到上面你选择的那个选项
    g.msgbox("你的选择是:"+str(choice),'结果') # 打印出来
    msg='你希望再来一次么?'
    title='请选择'
    if g.ccbox(msg,title):    #  ok为真  cancel为假
        pass
    else:
        exit(0)   # 用于退出程序  .
