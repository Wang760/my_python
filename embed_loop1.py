'''
嵌套循环
    l = [[1,2,3],[4,5,6],[7,8,9]]
    如何把l中所有元素打印出来
'''
l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in i:
        print(j)

for i in range(3):
    for j in range(5):
        print(f'i={i},sum={i*j}')

l = []
for i in range(1,4,2):
    item = []
    for j in range(5):
        item.append(j)
    l.append(item)
print(f'l={l}')

