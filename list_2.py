'''
列表学习2
    检查列表中是否包含某个数: 12 in my_list
    列表可以获取元素个数：len(my_list)
    列表可以用 + 拼接两个列表 new_list = my_list1 + my_list2
    列表也可以 * 表示某个列表重复  new_list = my_list * 2
    列表反序： my_list.reverse()
    列表最大值：max(my_list)
    列表最小值：min(my_list)
    使用sort()方法排序列表： my_list.sort()
'''
a = [1,2,12,4,5,6,7,8]
b = ["new","Hi","23","we"]
print(1 in a) #Bool: true
print(len(a))
print(a[len(a)-1])
print(a + b)
print(a*3)
print(a[::-1]) # 可以反向显示列表，但列表不变
a.reverse() # 列表被改动
print(f"a={a}")
print(a)
max_value = max(a)
print(max_value)
print(min(a))
a.sort()  #会更改列表
print(f"a={a}")

