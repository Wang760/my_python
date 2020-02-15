'''
元组tuple的学习
    元组是不可变类型
    元组可以做如下判断
        in tuple
        not in tuple
        max(tuple)
        min(tuple)
        tuple.index("a")
        tuple.count("a")
        len(tuple)
        也可以 + 拼接
        也可以截取
元组通常用来表示一些关联性非常强的数据，如x/y，color(255,255,255), key...

'''
a = (1,2,3)  #它可以不加()
print(type(a))
b = (5) # 这种情况b是INT类型
print(type(b))
b = (5,)
print(type(b))
c = 1,2,3
print(type(c))
print(c[::-1]) #元组倒叙排列

print(b + c)
print(max(b+c))

#元组可以给变量分别赋值
t = 1,2,3
a,b,c =t
print(f"t[0]={a} t[1]={b} t[2]={c}")


