#coding=utf-8
dic={'name':'heygor','QQ':914338492}
dic1={'name':'gaga'}
#直接访问
print(dic)
#数据筛选
print(dic['QQ'])

#删除字典
#del
dic={'name':'heygor','QQ':914338492}
print(dic)
del dic['QQ']
print(dic)
del dic
#print(dic)
#清空
#clear
dic={'name':'heygor','QQ':914338492}
print(dic)
dic.clear()
print(dic)

#修改
dic1={'name':'5kong','age':18}
print(dic1)
dic1['name']='tangsir'
print(dic1)
dic1['age']='gaga'
print(dic1)


#keys
dic1={'name':'5kong','age':18}
print(dic1.keys())

for i in dic1.keys():
    print(i)

#values
dic1={'name':'5kong','age':18}
print(dic1.values())
for i in dic1.values():
    print(i)

#items()
dic1={'name':'5kong','age':18}
print(dic1.items())

for key,value in dic1.items():
    print(key+':'+str(value))


























