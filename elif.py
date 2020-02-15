'''
if语句中可以添加elif处理多条件判段
    if A：
        代码...
    elif B:
        代码...
    elif C:
        代码...
    else:
        代码
'''
#根据用户输入成绩判断属于哪种类型
# 100   S
# 90 ~ 99 A
# 80 ~ 89 B
# 70 ~ 79 C
# 60 ~ 69 D
# 0 ~ 59 E

#1录入成绩
score = input("请输入成绩(0~100)： ")
if score !=" " and score != "":
    score = int(score)
    #2 根据成绩归类
    if score in range(100):
        if score == 100:
            print("你的成绩是: S !")
        elif score >= 90 and score <= 99:
            print("你的成绩是: A !")
        elif score >= 80 and score <= 89:
            print("你的成绩是: B !")
        elif score >= 70 and score <= 79:
            print("你的成绩是: C !")
        elif score >= 60 and score <= 69:
            print("你的成绩是: D !")
        else:
            print("你的成绩是: E !")
    else:
        print("输入错误！！！")
else:
    print("没有任何输入！！！")
