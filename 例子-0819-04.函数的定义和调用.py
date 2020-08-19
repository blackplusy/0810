#coding=utf-8
#函数的定义
def print_name():
    print('its kobe')
#函数的调用
print_name()

#函数赋值给变量
l=[1,2,3,4]
b=len
num=b(l)
print('列表中由元素%d个'% num)

#函数的常用格式
#1.无参数，无返回值
def print_name():
    print('我是高富帅！')
print_name()
#2.无参数，有返回值
def sleep():
    return 'im sleeping!!!'
s=sleep()
print(s)
#3.有参数，无返回值
def sub(x,y):
    print('x+y=',x+y)

sub(10,20)
#4.有参数，有返回值
def sub(x,y):
    return x+y
s=sub(5,13)
print(s)
