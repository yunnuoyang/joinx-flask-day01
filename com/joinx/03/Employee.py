#python的面向对象的类
class Employee:
    count=0
    name='employee'
    def EmpCount(self):
        self.count+=1
        return self.count
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("员工的姓名：",self.name,"薪水：",self.salary)
        return self
    def __del__(self):
        print(self.name,"销毁")
employee=Employee("joinx",18000)
employee.display()
employee=Employee("lucy",300000)
e2=Employee("zl",222222)
print(e2.EmpCount())
#销毁对象
del employee
del e2
try:
   employee.display()
except Exception:
    print("对象已经被销毁")
