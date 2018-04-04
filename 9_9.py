#chp1_9*9_九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print ("{}*{}={:2}".format(j,i,i*j),end='')
    print('')
