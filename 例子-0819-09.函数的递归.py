#coding=utf-8
#嵌套函数
def t1():
    print('im t1')
def t2():
    t1()
    print('im t2')
def t3():
    t2()
    print('im t3')

t3()
#t3--t2--t1--print--print--print

#递归例子：阶乘 n!=1*2*3*...n
def func(n):
    if n==1:
        return n
    elif n>1:
        return n*func(n-1)
    else:
        print('请输入大于0参数')

print(func(5))
#1.---->1
#2.-->2*func(1)  func(1)==1  -->2*1
#3.-->3*func(2)  func(2)==1*2 -->3*2*1

#递归例子:盗梦空间
def func(n):
    print('进入到第%d层梦境'% n)
    if n==3:
        print('进入到潜意识区')
    else:
        func(n+1)
    print('从第%d层梦境中醒来'% n)

func(1)

























