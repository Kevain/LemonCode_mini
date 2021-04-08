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
# print("hello,world123")

# age = 18.5
# age_str = "18.5"
# age_str2 = '18.5'
# person_info = "你好，我叫XXx，我来自XXX,我现在工作" \
#               "是XXx，我的项目是XXX,我负责的XXX"
# print(person_info[1::2])
# a=person_info.find("X")
# print(a)
# age = input("age:")
# name = input("name:")
# print("{}的年龄是{}岁".format(name, age))
my_int = 10
my_str = 'i"m python'  # 字符串 ，单引，双引，三引号都行，三引号不赋值算注释
my_touple = ("python", 33, 0.3)  # 元组，固定长度不能变
my_list = ['pythh', 12, 1.2, 3, 33, 9]  # 列表，可变长度，有序
my_dict = {'name': 'zhang', 'age': 28}  # 字典，无顺序，按key-value方式存储

# 一行可以写多个语句，用;分开就行
my_set = {1, 2, 3};
print(list(my_set))  # 集合，元素无重复
my_bool = True
a = b = c = 1  # 一个值给多个变量赋值
a, b, c = 1, 2, "linda"  # 同时多个值赋值给多个变量
