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
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3] )         # 输出第二个至第三个元素
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2 )      # 输出列表两次
print(list + tinylist)    # 打印组合的列表
print('输出元组')
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组
dict={}
dict['one']='this is one'
dict[2]='this is two'
tinydict={'name':'join','code':6374,'dept':'sales'}
print(dict['one'])
print(dict[2])
print('输出所有的键值')
print(tinydict.keys())
print('输出所有的值')
print(tinydict.values())

