#coding=utf-8
#读文件
#定义一个变量接受open函数打开文件后内容
#如果出现字符集问题通过设置encoding解决
file=open('F:\\1.txt','r',encoding='utf8')
print(file)
for i in file:
    print(i)
file.close()

#写文件
'''
str1='oh my dea baby!!'
file=open('f:\\memeda.txt','w')
file.write(str1)
file.close()
print('文件已经写入')
'''
file=open('f:\\memeda.txt','a')
file.write('\ncome on baby!!!')
file.close()
print('执行完毕')
