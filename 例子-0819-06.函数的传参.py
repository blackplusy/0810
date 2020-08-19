#coding=utf-8
#1.实参位置
def info(name,age):
    print('your name is %s,your age is %d' % (name,age))
info('lilei',20)
#info(20,'lily')


#2.关键字参数
def animal(pet1,pet2):
    print(pet1+'wang!'+pet2+'miao')
animal(pet2='cat',pet1='keji')

#3.参数默认值
def userinfo(name,age,minzu='汉'):
    print('您的名字%s,您的年龄%d,民族是%s' % (name,age,minzu))

userinfo('o8ma',90)
userinfo('ladeng',80,'v5er')

#4.不定长参数
def test(x,y,*args):
    print(x,y,args)

test(1,2,'o8ma','ladeng')

def test1(x,y,**args):
    print(x,y,args)

test1(1,2,a=10,b='gaga')
