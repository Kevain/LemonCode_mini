"""
@FileName：test_parameter.py
@Description：...
@Author：Ken
@Time：2021/4/12 21:03
"""
import random

import pytest


@pytest.mark.parametrize("x", [1, 2, 3])
def test_add(x):
    print(x)
    assert x == random.randrange(1, 4)
