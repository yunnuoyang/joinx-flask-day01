#写模式
fo =open("foo.txt","w")
fo.write("joinx test python io stream")
fo.close()
#读模式
fo=open("foo.txt","r+")
str=fo.readline(20)
print(str)
fo.close()

fo=open("foo.txt","r+")
str=fo.readline(3)
print("读取的字符",str)
posistion=fo.tell()
print("当前的文件读取的位置",posistion)
#将文件位置重新定位到文件开头
posistion=fo.seek(0,0)
str=fo.read(30)
print("重新定位后的字符串",str)
fo.close()
import os
#os.rename("foo.txt","joinx.txt")
#fo=open("abc.jpg","w")
os.remove("abc.jpg")
os.mkdir("newdir")