# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 15:30
# 文件名称：name_function.py
# 开发软件：PyCharm
def get_formatted_name(first,last,middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
