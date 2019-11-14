#time模块
import  time
ticks=time.time()
localtime=time.localtime(ticks)
print("当前时间戳",ticks)
print("当前时间",localtime)
localtime=time.asctime(time.localtime(time.time()))
print("格式化时间",localtime)
print( time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print( time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
#打印19年1月的所有信息
import calendar
cal=calendar.month(2019,1)
print(cal)
