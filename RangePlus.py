# 阶乘计算
sum,tmp =  0, 1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print ("运算结果是：{}".format(sum))
