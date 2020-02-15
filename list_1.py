'''
列表-list
   列表可以是任意元素 [1,"小明", B, True]
   列表索引是从0开始
   列表下表可以是负数，如 -1， 表示从最后一个元素
   列表是可以截取的
'''
a = [] #空列表
b = [1,3.14,"H", False,4,598,4.34]
print(type(b))
print(b[0])
print(b[2])
print(b[-1])
print(b[0:7:2]) #[start:end:step]
b[0] = "Hi"
print(b)

