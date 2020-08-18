


a='1234abcd'
#1.方法1
for i in range(1,len(a)+1):
    print(a[8-i],end="")
#2.方法2
for i in range(-len(a),0):
    print(a[-i-1],end="")
