'''
While 循环
    For循环可以准确控制循环次数
    而While循环可以用在不确定循环次数的情况下
    while 条件：
        语句1
        条件变化
    while控制的关键字是break 和 Continue
        循环中使用 Break 可以终止整个循环
        循环中使用 Continue 可以终止本轮循环，继续下一轮循环

        For i in range(5)：
            if i == 2：
                print("Hello!")
                break

        For i in range(5):
            if i % == 0:
                continue
            print("Hello!")
'''
# i = 0
# while i < 10:
#     print("Python")
#     i +=1

# l = []
# while True:
#     i = input("请输入客户信息(按q退出)")
#     if i == "q":
#         break
#     else:
#         l.append(i)
# print(f'您输入的客户信息是{l}')

l = []
i = ""
while i != "q":
    i = input("请输入您一天的计划(按q退出)")
    if i == "q":
        break
    else:
        l.append(i)
print(f'您一天的计划是{l}')
