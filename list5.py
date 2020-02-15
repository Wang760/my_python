'''
列表嵌套(二维列表)
    l1,l2,l3 = [12,26],["A", "Hi"],[Ture, Flase]
    my_list = [[12,26],["A", "Hi"],[Ture, Flase]]
    my_list = [
        [12,26],
        ["A", "Hi"],
        [Ture, Flase]
    ]
    获取列表中元素
        value = my_list[1][0] #元素 “A”
'''

stud1 = ["小明",95]
stud2 = ["小红",86]
stud3 = ["小张",67]

student = [
    stud1,
    stud2,
    stud3
]
print(student)
index = 2
print(f'{student[index][0]}的分数是:{student[index][1]}')

