#coding=utf-8
#insert
l=['a','b','c']
print(l)
l.insert(1,'d')
print(l)
l.insert(-2,'e')
print(l)

#extend
l1=[1,2,3,4]
print(l1)
l1.extend('a')
print(l1)
l1.extend([1,2,3])
print(l1)


#列表推导式
#1.给定列表
a=[1,2,3,4]
print([5*x for x in a])

#2.没有给定列表可以用range()函数
print([3*x for x in range(1,11)])

#3.使用if条件进行推导
a=[1,2,3,4]
print([x for x in a if x%2==0])

#4.多个for语句进行列表推导
print([[x,y] for x in range(2) for y in range(2)])











