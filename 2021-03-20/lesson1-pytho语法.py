"""
@FileName：lesson1-pytho语法.py
@Description：python基本语法
@Author：Ken
@Time：2021/3/20 14:44
"""

# 注释快捷键 ctrl+/
"""
多行注释  ”“”
查看源码 ctrl+B
调整代码格式 alt+ctrl+L
"""
print("hello,world123")

# age = 18.5
# age_str = "18.5"
# age_str2 = '18.5'
# person_info = "你好，我叫XXx，我来自XXX,我现在工作" \
#               "是XXx，我的项目是XXX,我负责的XXX"
# print(person_info[1::2])
# a=person_info.find("X")
# print(a)
age = input("age:")
name = input("name:")
print("{}的年龄是{}岁".format(name, age))
