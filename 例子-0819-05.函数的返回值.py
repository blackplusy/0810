#coding=utf-8
#1.一个返回值
#定义sum函数，需要传入2个参数
def sum(a,b):
    #业务逻辑，相加
    jisuan=a+b
    #返回计算结果
    return jisuan
#通过变量接收函数操作后的结果，注意，一定要传入2个参数
a=sum(20,30)
print(a)

#2.多个返回值
def ret(a,b):
    a*=10
    b*=100
    return a,b
num=ret(3,7)
print(num)
print(type(num))

num1,num2=ret(10,20)
print(num1,num2)
