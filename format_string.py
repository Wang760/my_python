'''
指定格式转换
F-string : {}
format() 
'''
name='老王'
age=48
result = "你好" + name +", "+"您今年已经" + str(age) +"岁了！"
print(result)
#用f进行格式转换
name='老王'
age=48
result = f"你好{name}, 您今年已经{age}岁了！"
print(result)
#使用format方法
result1 = "你好{}，您今年已经{}岁了！".format(name, age)
print(result1)
result2 = "你好{0}，您今年已经 {0} 岁了！".format(name, age)
print(result2)
