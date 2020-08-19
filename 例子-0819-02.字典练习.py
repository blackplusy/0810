#coding=utf-8
dic={'admin':'123','user1':'456','user2':'789'}
while 1:
    name=input('请输入用户名：')
    if len(name)==0 or name not in dic.keys():
        print('请重新输入')
    else:
        while 1:
            password=input('请输入您的密码:')
            if dic[name]==password:
                print('登录成功！！')
                break
            else:
                print('请重新输入')
        break
                
