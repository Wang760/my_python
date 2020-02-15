'''
这节练习是了解转义字符的应用
\
\\
\t
\n
\a
'''
#打印反斜线
my_string=('\\')
print(my_string)
#使用转义支符\n: 表示换行
my_string=('Hel\nlo')
print(my_string)
#使用转义字符\t: 表示tab空格
my_string='Hel\tlo'
print(my_string)
#用r阻止转义来显示原本字符串含义
my_string=r'\n 表示换行'
print(my_string)
#用'''来进行换行，可以保留原始字符串的原貌
my_string='<html>\n</html>'
print(my_string)
my_string='''<html>
    <head>
    </head>
</html>'''
print(my_string)