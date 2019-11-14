#自定义函数
def function01(parm):
    if(parm>0):
        print("当前值大于0")
    else:
        print("当前值小于0")
    return parm
print(function01(4))
def getUserById(id):
    if id==1:
        return "id为1的用户joinx返回"
    elif id==2:
        return "id为2的用户lucy返回"
    elif id ==3:
        return "id为3的用户bob返回"
    else:
        return "查无此人"
print(getUserById(2))
def chang(num):#值传递，不会改变本身
    num=3
    return num
num=2
print(chang(num))
print(num)
def objParams(*obj):#不定长参数，java中的..object
    return obj
print(objParams(1,2,3,'joinx'))
#lamda表达式
sum=lambda a,b:a+b;
print(sum(3,4))
