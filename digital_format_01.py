'''
波波教学17-进行数字格式化
'''
pi=3.1415926
#[(填充)对齐] [符号] [宽度] [.精度] [类型]
result = f"圆周率 {pi} 是一个无限不循环小数"
print(result)
#精度，类型控制
result = f"圆周率 {pi:.4f} 是一个无限不循环小数"
print(result)

#宽度控制
result = f"圆周率 {pi:50.4f} 是一个无限不循环小数"
print(result)

#符号控制
result = f"圆周率 {pi:+50.4f} 是一个无限不循环小数"
print(result)

#向左对齐控制
result = f"圆周率 {pi:<+50.4f} 是一个无限不循环小数"
print(result)

#中间对齐控制
result = f"圆周率 {pi:^+50.4f} 是一个无限不循环小数"
print(result)

#填充控制
result = f"圆周率 {pi:-^+50.4f} 是一个无限不循环小数"
print(result)

#表示成百分数形式
result = f"圆周率 {pi:%} 是一个无限不循环小数"
print(result)

#表示成百分数形式，但保留小数点两位
result = f"圆周率 {pi:.2%} 是一个无限不循环小数"
print(result)

#表示成其他进制的数值
pi = 25

#二进制转换
result = f"转换为二进制 {pi:#b} 数"
print(result)

#二进制转换，但不需要前面的'B'
result = f"转换为二进制 {pi:b} 数"
print(result)

#十六进制转换
result = f"转换为十六进制 {pi:#x} 数"
print(result)

#八进制转换
result = f"转换为八进制 {pi:#o} 数"
print(result)

#八进制转换加填充
result = f"转换为八进制 {pi:*^08x} 数"
print(result)

'''
练习1：
将1~256的整数以此转换成二进制，八进制，十六进制，并对齐打印
'''
print(f'整数  二进制   八进制   十六进制')
for i in range(6):
    print(f'{i:>03d}  {i:>08b}    {i:>03o}    {i:>04x}')

