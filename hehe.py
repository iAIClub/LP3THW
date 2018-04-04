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