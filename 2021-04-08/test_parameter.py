"""
@FileName：test_parameter.py
@Description：...
@Author：Ken
@Time：2021/4/12 21:03
"""
import random

import pytest


# @pytest.mark.parametrize("x", [1, 2, 3])
# def test_add(x):
#     print(x)
#     assert x == random.randrange(1, 3)
def bubble_sort(nums):
    for i in range(nums - 1):
        for j in range(nums):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return random.choice([nums, None, 10])


def test_bubble():
    assert bubble_sort(1) == 1
    assert bubble_sort(3) == 4


if __name__ == '__main__':
    pytest.main(['-s', 'test_parameter.py'])
