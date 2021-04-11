"""
@FileName：unitTest_example.py
@Description：...
@Author：Ken
@Time：2021/4/11 11:55
"""
import unittest


class simple_test(unittest.TestCase):
    def setUp(self):
        print("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def tes_lst(self):
        print('test_lst')
        self.assertEqual(self.foo.pop(), 9)

    def test_2nd(self):
        print("test_1nd")
        self.assertEqual(self.foo.pop(), 9)

    def tearDown(self):
        print("end method")
