'''
    For的练习题
        练习一：提示用户输入5个数，组成列表；并将列表的各个元素 x2, 计算这个新列表的所有元素的和

        练习二：找出100以内所有7的倍数以及包含7的数，将它们放在一个列表中
'''
#练习一
l = list()
sum = 0
for i in range(5):
    value = input(f"请输入第{i+1}个数")
    l.append(float(value))
print(l)
for i in l:
    sum += float(i*2)
print(sum)

#练习二
l = list(range(1,101))
#result = list()
result = []
for i in l:
    if i % 7 == 0 or i % 10 == 7 or i // 10 % 10 ==7:
        result.append(i)
print(result)
print(len(result))