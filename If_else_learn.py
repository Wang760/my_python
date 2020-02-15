'''
if 是流程控制语句，用来做判断
如果条件符合，就执行后面语句
if语句格式要求使用冒号和缩进
   if A：
       代码
   else:
       代码
if语句可以嵌套
'''
#接受控制台的输入，判断是否是偶数
#1 输入数据
number = input('请输入整数: ') 
number = int(number)
#2 判断是否是偶数
result = number % 2
print(result)
if result == 0: 
    print(f'你输入的数字{number}, 是一个偶数!')
    #3 判断这个数可以被3整除
    if number % 3 == 0:
        print("这个数还可以被3整除!")
else:
    print(f'你输入的数字{number}, 是一个奇数!')

print('End')
