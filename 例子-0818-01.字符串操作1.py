#coding=utf-8
#字符串的索引
name='im your baba!!!'
print(name[0])
print(name[3])
print(name[-2])
#print(name[30])

#字符串的切片
'''
name='im your baba!!!'
print(name[0:4])
print(name[:4])
print(name[4:])
print(name[3:-1])
'''
#字符串拼接
a='lady'
b='gaga'
print(a+b)
print(a+b[-1])
tel='0452-1111111'
print(tel[:5])
print(tel[5:])
print(tel[:5]+'6'+tel[5:])

#字符串的遍历
name='im your papa!!'
for i in name:
    print(i)

#去空格
'''
string.strip()   去掉两边的空格
string.lstrip()  去掉左边的空格
string.rstrip()  去掉右边的空格

'''
str1='   python   '
print(str1)
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

#计算长度
str1='   python   '
print(len(str1))




