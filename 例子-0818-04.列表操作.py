#coding=utf-8
#直接访问
l1=['李元芳','钟馗','李白']
print(l1)
#遍历访问
for i in l1:
    print(i)
#成员访问
if '张小敬' in l1:
    print('here')
else:
    print('not here!!')
#列表的索引和切片
l1=['马超','关羽','张飞','黄忠','云云']
print(l1[0])
print(l1[-2])
#print(l1[5])
print(l1[2:])
print(l1[2:3])

#列表的拼接
l=[1,2,3,4]
m=['a','b']
print(l+m)
print('*'*20)
#列表的更新
l=[1,2,3]
print(l)

l[2]='柳岩'
print(l)

l[-3]='刘亦菲！'
print(l)

#列表的删除
l=[1,2,3]
del l[2]
print(l)

del l
#print(l)
#栈的方式访问列表
l=[1,2,3,4]
print(l)
l.append('a')
print(l)
l.append(5)
print(l)
l.pop()
print(l)
l.pop()
print(l)
#获取列表的索引
l=['a','b','c','d']
print(l.index('c'))

l=['a','b','c','d']
for index,value in enumerate(l):
    print('索引是'+str(index)+',值是'+str(value))
#列表的排序
l=[1,2,3,4]
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
l.sort()
print(l)
l.reverse()
print(l)


l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)




















































