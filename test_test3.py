# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 11:11
# 文件名称：test_test3.py
# 开发软件：PyCharm
import unittest
from test3 import Employee

class TestEmplpyee(unittest.TestCase):
    def setUp(self):
       self.person = Employee('cui','yaxie',100000)

    def test_give_default_raise(self):
        self.person.give_raise()
        self.assertEqual(self.person.annual_salary,105000)

    def test_give_custom_raise(self):
        self.person.give_raise(50000)
        self.assertEqual(self.person.annual_salary,150000)

unittest.main()
