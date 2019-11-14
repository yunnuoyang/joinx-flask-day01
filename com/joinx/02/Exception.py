try:
    var=3/0
except ZeroDivisionError:
    print("除零异常")
finally:
    print('异常处理结束')
# raise [Exception]
def function(level):
    if level <1:
        raise Exception("level小于1",level)
    else:
        return 0
print(function(00))