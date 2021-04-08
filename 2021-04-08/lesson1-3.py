"""
@FileName：lesson1-3.py
@Description：...
@Author：Ken
@Time：2021/4/8 23:15
"""
my_str = "I LOVE PYTHON"
my_list = ["python", "java", "lanuage", "age"]
my_list2 = [24, 12, 2.2, 9.8]
my_tuple = ("python", 33, "java", 20)
my_dict = {"name": "linda", "age": 99}
my_list1 = ['a', 'b', 'a', 1, 1, 2, 3, 3]
my_set = (1, 2, 3)

# print(tuple(my_list))
# print(list(my_tuple))
# print(set(my_list1))    # 列表转成set变成不重复的
# print(set(my_dict))     # 字典类型转成set只有key值
# print(list(my_dict.values()))   # 字典转换成列表，key/value可以单转
# print(list(my_dict))
my_tuple1 = ('one', 1), ('two', 2), ('three', 3)
my_ilst_tuple = [('one', 1), ('two', 2), ('three', 3)]
print(my_tuple1)
print(type(my_ilst_tuple))
print(dict(my_ilst_tuple))
