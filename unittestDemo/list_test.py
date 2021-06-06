# -*- coding: utf-8 -*-
"""
@FileName：list_test.py
@Description：
@Author：Ken
@Time：2021/5/22 22:13
列表、字典、元组、集合
"""
# l = ["a", "b", "a", 1, 2, 3, 4, (11, 22, 33), 2, 3, 4, ]

# def fun(a):
#     if len(a) > 3:
#         return a[3:]
#     else:
#         return a[0:2]


# print(fun(l))
# def fun1(s):
#     a = set(s)
#     return list(a)
#
#
# print(fun1(l))
# print(len(l))
# print(len(fun1(l)))
# def fun3(a):
#     l1 = []
#     for i in a:
#         if i not in l1:
#             l1.append(i)
#     return l1
#
#
# print(fun3(l))
# dict1 = {"a": "123", "bb": 234, 'cccc': 456}
# dict2 = {"b": "13", "c": 34, 'cc': 456}
# str1 = str(dict1)

# 字符串转为字典类型
# print(eval(str1), type(eval(str1)))

# 一次性输出键值对 items
# for i, j in dict1.items():
#     print(i, j)

# 创建一个新的字典 fromkeys
# str2 = ['a', 'b', 'c']
# dict3 = {}
# dict4 = dict3.fromkeys(str2,123)
# print(dict4)

# ##############集合 set
# set1 = {1, 2, 3, 4, 5}
# set1.add(11)
# set1.update({1, 23, 333})
# set1.remove(1)
# print(set1, type(set1))

'''
循环
'''


# def sum(a, b):
#     s = 0
#     for i in range(a, b):
#         s = s + i
#         i += 1
#     return s
#
#
# a=sum(0, 101)
# print(a)

def aa(*args, **kwargs):
    print(args)
    print(kwargs)


aa(1, 2, 3, 4, 5, a=11, b=12, c=13)
