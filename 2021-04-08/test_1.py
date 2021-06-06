# -*- coding: utf-8 -*-
"""
@FileName：test_1.py
@Description：
@Author：Ken
@Time：2021/6/6 21:21
"""

# python实现石头剪刀布游戏
import random

a = (int(input("请出拳--石头1 剪刀2 布 3  ")))
com = random.randint(1, 3)
if (com == 1 and a == 2) or (com == 2 and a == 3) or (com == 3 and a == 1):
    print("电脑赢")
elif com == a:
    print("平局")
else:
    print("你赢")
