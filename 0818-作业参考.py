#coding=utf-8
#1.菱形
'''
for i in range(-3,4):
    if i<0:
        a=-i
    else:
        a=i
    print(' '*a+'*'*(7-a*2))

#2.菱形
n=int(input('请输入一个数字'))
c=n//2
print(n)
print(c)
for i in range(-c,c+1):
    a=-i if i<0 else i
    print(' '*a+'*'*(n-2*a))
'''
#3.对顶三角
n=7
e=7//2   #3
for i in range(-e,n-e):
    a=-i if i<0 else i
    print((e-a)*' '+'*'*(2*a+1))
    
