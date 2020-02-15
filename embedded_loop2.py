'''
嵌套循环练习题
    1，找到100~1000内的最小的水仙花数
    水仙花数：每位上的数字的3次幂之和等于数字本身
    例如：407 = 4**3 + 0**3 + 7**3
    2，找出100以内所有质数
    质数：大于1，并且只能被1和它本身整除的数
    3，打印出99乘法表
    1*1=1  1*2=2  1*3=3  ...   1*9=9
    2*1=2  2*2=4  2*3=6 
    3*1=3
    ...
    9*1=9                      9*9=81
'''
#练习一
l = []
for i in range(100,1000,1):
    a = i%10 #个位
    b = (i//10)%10 #十位
    c = (i//100)%10 #百位
    if i == a**3 + b**3 + c**3:
        l.append(i)
print(f'100~1000内的最小水仙花数有{min(l)}')

#练习二
l = []
# for i in range(2,40000):
#     for j in range(2,i):
#         if i%j == 0 : 
#             break
#         else:
#             if j == (i-1):
#                 l.append(i)
# print(f'100以内所有质数有{l}')
for i in range(2,100):
    is_prime = True
    for j in range(2,i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        l.append(i)
print(f'100以内所有质数有{l}')


#练习三
for i in range(1,10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j:2d}',end="   ")
    print("")