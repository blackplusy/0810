#coding=utf-8
#find
a='c'
str1='aabbcc'
print(str1.find(a))
a='d'
print(str1.find(a))
#index
a='b'
print(str1.index(a))
a='d'
#print(str1.index(a))

#isalpha()
a='simida'
print(a.isalpha())
a='simida1'
print(a.isalpha())

#isdigit()
a='123'
print(a.isdigit())

#upper()和lower()
name='Apple'
print(name.upper())
print(name.lower())

#startswith()和endswith()
a='aabbcc'
print(a.startswith('a'))
print(a.endswith('b'))

#count()、replace()、split()
name='heygorgaga'
print(name.count('a'))
print(name.replace('g','memeda'))

name='1,2,3,4'
b=name.split(',')
print(b)

#引号
print('我是你dady！')
print("我是你巴比")

#print('i'm your papa')
print("i'm your papa")
print('i\'m your mom')

'''
这段代码不生效
'''
print('''
我的家在
东北
松花江上！
''')














