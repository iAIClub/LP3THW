# 下列代码是用于计算WQM的T和C的N值----
import sys
from sympy import *
from sympy.abc import x,y,a,b,c,d,e,f,g,h,i,j,k
x = symbols('x')#本案例中N值设置为x。
TA0=symbols('TA0')
TA1=symbols('TA1')
TA2=symbols('TA2')
TA3=symbols('TA3')

T1=symbols('T1')
T2=symbols('T2')
T3=symbols('T3')
T4=symbols('T4')
T5=symbols('T5')
T6=symbols('T6')
T7=symbols('T7')
T8=symbols('T8')
T=symbols('T')

d=symbols('d')
d1=symbols('d1')
d2=symbols('d2')
d3=symbols('d3')
N=symbols('N')

G=symbols('G')
H=symbols('H')
II=symbols('II')
J=symbols('J')
WBOTC=symbols('hh')
Tcor=symbols('Tcor')

C1=symbols('C1')
C2=symbols('C2')
C3=symbols('C3')
C4=symbols('C4')
C5=symbols('C5')
C6=symbols('C6')
C7=symbols('C7')
C8=symbols('C8')
C=symbols('C')

DDL=symbols('DDL')
hh=symbols('hh')

p1=symbols('p1')
p2=symbols('p2')
p3=symbols('p3')
p4=symbols('p4')
p=symbols('p')




# ----下面是一个接受用户输入，给4个系数赋值的过程---
print ('''
-------------------- 准备计算温度的N值 ------------------
-------------------- 第1步:参数输入 ---------------------
请依次输入4个参数:TA0  TA1  TA2  TA3；每数间有一个空格！
例如：6.643511e-05 2.742823e-04 -2.452346e-06 1.531625e-07
''')

TA0,TA1,TA2,TA3 = map(float,input("\n请输入：>").split())

print ('''
\n-------------------- 第2步：温度点输入 ---------------------
请依次输入8个温度点；35—----—0；每数间有一个空格！
例如：34.8892 29.9992 24.9242 20.0569 15.0870 9.8717 4.8089 0.8130
''')

# 接受一组8个温度点输入。

T1,T2,T3,T4,T5,T6,T7,T8 = map(float,input("\n请输入：>").split())
T = T1,T2,T3,T4,T5,T6,T7,T8 #将数组赋值给T

#-----------下面是利用一个循环依次计算并打出N值---------------------------
print ("\n--------------------温度的N值为:--------------------")

for i in range (0,8):
    d = solve( [TA0 + TA1 *x + TA2*(x **2) +TA3 *(x **3) - 1/(273.15+T[i])], [x]) # 核心计算公式。使用T[i]从T这个数组中按照索引取出数据。
    d1,d2,d3 = d # 将数组d进行切片。
    N = 2.718281825 **d1 #转换出N值
    print (round(N))# "N值为："

print ("\n-------------------- 计算结束 ---------------------")

# -------------------------------------- 以下是电导率部分的计算-----------------------------
print ('''
*******************下面开始计算 电导率 的N值 *******************
-------------------- 第1步:参数输入 --------------------
请依次输入G～ H～ II～ J～ WBOTC～ hh～ Tcor；每个数间有一个空格。
例如：-1.010158e-00 1.570058e-01 -3.719996e-04 5.332862e-05 -7.2130e-07 0 3.250000e-06
''')

# 输入参数
G,H,II,J,WBOTC,hh,Tcor = map(float,input("\n请输入：>").split())
# 接受一组8个C值输入。注意：此处的C也是电导率，不过此处的C是DDL／10 单位不一样。

print ('''
--------------------  第2步：C值点输入 --------------------
请依次输入8个C点；每数间一个空格。
例如：6.40907164179105 5.87777849315069 5.33772534246575 4.83269173913044 4.33182356164383 3.82470607843137 3.35382323943662 2.994738522727287
''')

C1,C2,C3,C4,C5,C6,C7,C8 = map(float,input("\n请输入：>").split())

C = C1,C2,C3,C4,C5,C6,C7,C8 #将数组赋值给C

print ("--------------------电导率的N值为：--------------------")

for i in range (0,8):
    DDL = C[i]* (1+ Tcor*T[i])# T(i,2)其实是第二列数据，即电导率(单位s/m),此处重新命名为DDL
    p = solveset(G + hh *x + H*(x **2) + II *(x **3) + J*(x **4) - DDL, x)
    p1,p2,p3,p4 = p
    N =p2 *1000/sqrt(1+T[i]*WBOTC)
    print(round(N,3))

print ("\n*********************************** 电导率的N值计算结束（THE END）***********************************************")

# 本代码于20180227创建，并调试通过。
# 20180605上午增加了sys.setrecursionlimit和sympy的递归深度测试。
# 210800606重写 发现到了83行 N = 2.718281825 **d1，由于d1的数据类型是tuple，这里不支持乘方。
