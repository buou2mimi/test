# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 19:42
# 文件名称：survey.py
# 开发软件：PyCharm
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def stored_response(self,new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            print('-{}'.format(response))