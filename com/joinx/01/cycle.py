#循环语句
from click._compat import raw_input

list={1,2,3,4,5,6,7,8,9,0}
for i in list:
    print(i)
print('=======二位数组打印')
lists=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(lists)):
    for j in range(len(lists[0])):
        print(lists[i][j])
print("========while循环")
numbers=[12,32,12,34,55]
even=[]
odd=[]
while len(numbers)>0:
    number=numbers.pop()
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)
var=1
while var < 5:
    #num = raw_input("enter a number")
    print(var)
    var += 1
    #num -= 1
# for 循环语句
for letter in 'Python':
    print('当前字母', letter)
fruits=['banana','apple','mango']
for fruit in fruits:
    print('word now is',fruit)
for index in range(len(fruits)):
    print('当前索引值',fruits[index],index)
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')