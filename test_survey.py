# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 10:06
# 文件名称：test_survey.py
# 开发软件：PyCharm
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.stored_response('English')

        self.assertIn('English',my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What lanuage did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.stored_response(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)

unittest.main()