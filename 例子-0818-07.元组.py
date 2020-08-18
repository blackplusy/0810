#coding=utf-8
#创建元组
tup=(1)
print(tup)
print(type(tup))

tup=(1,)
print(tup)
print(type(tup))

#访问元组
a=(1,2,3)
print(a)

for i in a:
    print(i)

if 3 in a:
    print('3 is here')

#删除元组
a=(1,2,3)
del a
#del a[1]
#print(a)

#元组的索引和切片
a=(1,2,3,4,5)
print(a)
print(a[0])
print(a[-2])
print(a[2:4])
print(a[3:])
#补充
tup=(1,2,3,4,5)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(3))
print(tup.count(3))











