'''
练习一
提示用户输入任意年份，判读是否是闰年
满足条件之一：
  1，  能被400整除
  2，  能被4整除但不能被100整除
'''
#1 提示用户输入
# year = input("请输入年份 ")
# year = int(year)
# #2 判读400整除，判读4整除但不能被100整除
# result1 = year % 400
# result2 = year % 4
# result3 = year % 100

# if result1 ==0:
#     print(f"{year} 是闰年")
# elif result2 ==0 and result3 != 0:
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 不是闰年")

# '''
# 练习二
# 提示用户输入一个1 ~ 99999之间的整数，分别显示这个数字的个十百千万上的数字
# '''
# #1 提示用户输入有效数字
# number = input("请输入一个1 ~ 99999之间的整数 ")
# number = int(number)
# #2 分离个位
# #   个位 a1 = 123 % 10 
# #  十位 a1 = 123 // 10 % 10
# #  百位 a2 = 123 // 100 
# a1 = number % 10
# a10 = number // 10 % 10
# a100 = number // 100 % 10
# a1000 = number // 1000 % 10
# a10000 = number // 10000 % 10

# print(f"个位 {a1}")
# print(f"十位 {a10}")
# print(f"百位 {a100}")
# print(f"千位 {a1000}")
# print(f"万位 {a10000}")

'''
实现垂头剪刀布的游戏
1，玩家输入1，2，3分别代表剪刀，石头和布
2，程序随机选择剪刀，石头和布
3，在Python中实现随机数生成
    import random
    number = random.randint(1,3)
'''
import random 

number = random.randint(1,3)

my_input = input("玩家输入 \n1 石头 \n2 剪刀 \n3 石头\n ")
my_input = int(my_input)

if (my_input == number):
    print("平局")
else:
    if (my_input == 1) and (number ==2):
        print("玩家lost!")
    elif (my_input == 1) and (number ==3):
        print("恭喜你，win!")
    elif (my_input == 2) and (number ==1):
        print("恭喜你，win!")
    elif (my_input == 2) and (number ==3):
        print("玩家lost!")
    elif (my_input == 3) and (number ==1):
        print("玩家lost!")
    else:
        print("恭喜你，win!")
print(f"游戏是{number}")
