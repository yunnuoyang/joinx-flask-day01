print(__name__) #打印当前的__name__
import sys; x = 'runoob'; sys.stdout.write(x + '\n') #同一行显示多条数据使用;
x='a'
y='b'
print(x)
print(y) #换行输出
print('=======')
print(x),
print(y)
print('=====')
print(x,y) #不换行输出
print('截取字符串实例')
str='abcdefg'
print(str[1:5])
print(str * 2)#输出两次
print(str+'ppppp')#+号做连接符
letters=['a','b','c','v','b','n','m']
print(letters[1:6:2])#最后的参数为截取的步长 1 b 4 b 步长2 截取到v
