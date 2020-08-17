#coding=utf-8
#设置字符集
#相当于是翻译官
#中文的字符集常用GBK2312
#1.直接输出(通过print函数)
#数字  123
#字符串  abc
print('哈勒少~~~')
print(1000)
#2.变量输出
#变量：可以变化的值，理解为一个容器
#注意: python中所有的符号都是英文
a='告诉你妈妈今天晚上不回家,我给你看我写的代码'
#a相当于变量的名字,等号后面的值相当于变量的值
#通过print函数对数据和变量进行输出
print(a)
a=100
print(a)
#变量操作后输出
a=100
b=200
print(a+b)
a='黑哥 '
b='真帅'
print(a+b)
#3.函数输出
#系统中会有很多自带函数可以进行操作
#abs() 绝对值
#len()长度,元素个数
print(abs(-20))

s='爱你么么哒！'
print(len(s))
#4.格式化输出
# %s 接受变量传进来的字符类型数据
# %d 接受变量传进来的数值类型数据
# 输出内容如果只有一个变量可以不加括号，多个一定要加括号
#小明是no.1
#小红是no.2
#小刚是no.3
name='heygor'
num=1
print('%s is no.%d'%(name,num))
name='小红'
print('%s is no.%d'%(name,num))
print('your name is %s '% name)






















