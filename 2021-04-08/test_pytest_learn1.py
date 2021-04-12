"""
@FileName：test_pytest_learn1.py
@Description：...
@Author：Ken
@Time：2021/4/11 13:34
"""
import time

import pytest


def add(x, y):
    return x + y


def test_add():
    assert add(2, 3) == 5


def test_add2():
    print("2222222222222")
    time.sleep(3)
    assert add(11, 3) == 14.1
    assert add(4, 4) == 8


if __name__ == '__main__':
    pytest.main(['-s', 'test_pytest_learn1.py'])  # 调用pytest的main函数执行测试
