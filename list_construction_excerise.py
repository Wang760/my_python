'''
列表推导式练习
练习一：获取['food','Moon','Loop']中每个元素的首字母，并将首字母组成新的字符串
练习二：
        l1 = [2,4,6,8,10,12]
        l2 = [3,6,9,12]
        找出同时在l1和l2中的元素
练习三：将[1,3,5,7,9]中所有元素打印在控制台上
'''
#练习一
my_list = ['Food','Moon','Loop','def','My_oii']
# n = 0
# l,l1 =[],[]
# while n < len(my_list):
#     l = [i for i in my_list[n]]
#     n +=1
#     l1.append(l[0])
r1 = [i[0] for i in my_list]
print(''.join(r1))

#练习二
l1 = [2,4,6,8,10,12]
l2 = [3,6,9,12]
value = [i for i in l1 if i in l2]
print(value)

#练习三
l = [1,3,5,7,9]
# for i in l:
#     print(i)
[print(i) for i in l]