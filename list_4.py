'''
对列表的增加和删除
    增加新元素
        向列表末尾增加元素：my_list.append(5)
        向列表任意位置加入元素：my_list.insert(2, "HI")
        向列表末尾追加多个元素：my_list.extend([3,4,5])
    删除元素
        移除列表中最后一个元素：my_list.pop()
        移除列表中任意位置元素：my_list.pop(2)
        移除列表中任意位置元素：del my_list[2]
        移除列表内容：my_list.remove("b")
        清口列表：my_list.clear()
'''
a = [1,2,3]
a.extend([4,5,6,7])
print(a)
a.insert(len(a)-2, 2.5)
print(a.index(2.5))

b = ["hi","I am","We","You"]
s = "hello world"
b.extend(s)
print(b)
b.extend([s]) #带[]后，整个字符串会被当做列表
print(b)

#移除练习
a = [1,2,3,4,5]
value = a.pop()
print(a)
print(f"移除的元素是{value}")

value = a.pop(2)
print(a)
print(f"移除的元素是{value}")

#移除练习
#把列表中用户输入的字符串删掉

b = [1,2,3,"3",4,"3","3",5]
my_str = input("please input a number ")
my_str = str(my_str)
number = b.count(my_str)
print(number)
if number == 0:
    print(f"列表中没有{my_str}")
    print(b)
else:
    my_index = b.index(my_str)
    c = b.pop(my_index)
    print(c)
    number -= 1
    if number == 0:
        print(f"列表中没有{my_str}")
        print(b)
    else:
        my_index = b.index(my_str)
        c = b.pop(my_index)
        print(my_index)
        number -= 1
        if number == 0:
            print(f"列表中没有{my_str}")
            print(b)
        else:
            my_index = b.index(my_str)
            c = b.pop(my_index)
            print(c)
            number -= 1
            if number == -1:
                print(f"列表中没有{my_str}")
                print(b)
            else:
                print("循环太多，无法完成")






