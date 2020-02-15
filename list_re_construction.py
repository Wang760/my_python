'''
列表推导式用于快速构建新的数据列表
    [表达式 for 变量 in 列表]
    [表达式 for 变量 in 列表 if 筛选条件]
    l = [i // 2 for i in range[10] if i%2 == 0]
'''
l = [1,2,3,4]
l1 = [i*2 for i in l]
print(l1)

l2 = [i // 2 for i in range(50) if i%2==0]
print(l2)

l3 = [i for i in range(100) if i%2==0]
print(l3)

l4 = [i.upper() for i in "hello"]
print(l4)

