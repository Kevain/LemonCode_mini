"""
@FileName：lesson1-2 python语法.py
@Description：...
@Author：Ken
@Time：2021/3/31 23:55
"""

my_str = "I LOVE PYTHON"
my_list = ["python", "python", "java", "language", "age"]
my_list2 = {21, 12, 22, 3.1, 9.2, 22, 3.1, 9.2, "a", "a", "b", "b"}
my_tuple = ("python", 33, "jjave")
my_dict = {"name": "ken", "age": 20}
my_list1 = {"a", "b", "a", 1, 2, 3, 4, 3}
my_set = {1, 3, 2}

a = 10
# print(type(a))

# a1 = str(a)  # 强制转换从INT到STR
# print(type(a1))
# print(tuple(my_list))
# print(tuple(my_list1))
# print(tuple(my_list2))
# print(list(my_tuple))
# print(set(my_list))   # 列表转成set变成不重复的
print(set(my_dict))  # 字典类型转成set只有key值
print(list(my_dict.values()))  # 字典转成列表，key,value可以单转
print(list(my_dict))
my_tuple1 = ('one', 1), ('two', 2), ('three', 3)
my_list_tuple = [('one', 1), ('two', 2), ('three', 3)]
# print(my_tuple1)
print(type(my_list_tuple))
print(dict(my_list_tuple))

# 将对象 x 转换字符串

b = {"name": "linda", "age": 18}
str_b = repr(b)
print(str_b[0:3])

# 用来计算在字符串中的有效Python表达式,并返回一个对象
a = "[1,2,3]"
list_a = eval(a)
print(list_a[0])
