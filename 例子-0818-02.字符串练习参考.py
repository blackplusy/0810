#coding=utf-8

str1=input('请输入您的字符串')

# if str1=='':
if len(str1)==0:
    print('您的输入为空')
else:
    if str1[0] in 'aeiouAEIOU':
        print(str1+'ay')
    else:
        print(str1[1:]+str1[:1]+'ay')
