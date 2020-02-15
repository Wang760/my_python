'''
    学习快速建立列表的方法
        range的使用
            l1 = list(range(100)) # [0,1,2,3,...99]
        range可以生成 0 ~ end 之间的整数，不包含 end

        range(start,end)生成Start to End之间的整数，如 range(4, 12)
        range(start, end, step)生成步长为step的整数，如 range(4,12,2)
'''
l = range(100)
print(f'l的类型是: {type(l)}\n{l}')
l1 = list(l)
print(l1)


