# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 10:56
# 文件名称：test3.py
# 开发软件：PyCharm
class Employee():
    def __init__(self,first,last,annual_salary):
        self.first = first.title()
        self.last = last.title()
        self.annual_salary = annual_salary

    def give_raise(self,increase = 5000):
            self.annual_salary += increase