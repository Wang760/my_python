'''
print('Hello, world!')
print(12)
print('please input your name: ')
name = input()
print('hello '+ name)
'''

hp = 3814
max_hp=3480
result= int(hp/max_hp)
result *=100
print(str(result) + '%')

my_string = 'hello, world!'
print(my_string[::-1])
print(my_string[:3])
print(my_string[3:])
print(len(my_string))
print(my_string.find('a'))
print(my_string.count('a'))
is_in = 'hello' in my_string
print(is_in)
my_new_string=my_string.replace('o','-')
print(my_new_string)
length=len("王峰".encode('utf-8'))
print(length)
index = my_new_string.find('-')
print(index)

new_string='123,456,789'
children=new_string.split(',')
print(children)



