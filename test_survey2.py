# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 10:42
# 文件名称：test_survey2.py
# 开发软件：PyCharm
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.stored_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.stored_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()