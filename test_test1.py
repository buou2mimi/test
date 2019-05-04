# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 16:45
# 文件名称：test_test1.py
# 开发软件：PyCharm
import unittest
from test1 import site

class Test1TestCase(unittest.TestCase):
    def test_city_country(self):
        specific_location =site('chengdu','china')
        self.assertEqual(specific_location,'Chengdu,China')

    def test_city_country_population(self):
        specific_location = site('chengdu','china','10000000')
        self.assertEqual(specific_location,'Chengdu,China -population 10000000')
unittest.main()