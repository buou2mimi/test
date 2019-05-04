# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 15:33
# 文件名称：names.py
# 开发软件：PyCharm
from name_function import get_formatted_name
print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("\nPlease give me a last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print("\nNeatly formatted name:{}.".format(formatted_name))