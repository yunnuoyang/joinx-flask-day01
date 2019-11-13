#python的运算符
a=21
b=20
c=3
c=a+b
print("a+b的值为",c)
print("a-b的值为",a-b)
print("a*b的值为",a*b)
print("a/b的值为",a/b)
print("a%b的值为",a%b)
#修改变量abc
a=3
b=3
c=a**b
print("a**b的值为",c)#3的3次方
print("a//b的值为",27//3)#27开根号3
a=21
b=10
c=0
if a==b:
    print("a==b")
else:
    print("a!=b")
if a>b:
    print("a>b")
else:
    print("a<b")
a=1
b=1
c=3
if a>=b:
    print("a>=b")
else:
    print("a<b")
#赋值运算符的操作
a=21
b=10
c=0
c=a+b
d=0
print("a+b=",c)
d+=a
print("d+=a",d)
#移位运算与java相同
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)


c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)


c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)


c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)


c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)


c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)
#python逻辑运算符
a=10
b=20
if a and b:
    print("a and b都为 true",a,b)
else:
    print(a,"a,b有一个不为true===",b)
if a or b:
    print("a,b都为true,或a,b有一个为true")
else:
    print("a,b 都不为true")
a=0
b=0
if a and b:
    print("a,b都为true")
else:
    print("a,b有一个不为true")
if a or b:
    print("a,b都为true,或者有一个为true")
else:
    print("a,b 都不为true")
if not(a and b):
    print("a,b都为false,或者其中有一个变量为false")
else:
    print("a,b 均为true")
a=1
b=20
list=[1,2,3,4,5,6,7]
if a in list:
    print("a 在list集合中")
else:
    print("a 不在list集合中")
if b not in list:
    print("b 不在list集合中")
else:
    print("b 在list集合中")
#身份运算符
#is判断两个标识符是不是引用自一个对象，返回值为true或false
a=10
b=10
if a is b:
    print("a和b有相同的标识")
    print(a is b)
a=20
if a is not b:
    print("a和b没有相同的标识")
print(a==b)
a=1
while a<7:
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")
    a+=1