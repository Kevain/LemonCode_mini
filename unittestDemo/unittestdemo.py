"""
@FileName：unittestdemo.py
@Description：...
@Author：Ken
@Time：2021/4/13 23:15
"""
import unittest


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法")

    def setUp(self):
        print("这是每一个测试方法前面运行的方法，准备数据")

    def tearDown(self):
        print("这是每一个测试方法后面运行的方法")

    def test_one(self):
        print("测试方法1")
        self.assertIn('l', 'hello')

    def test_two(self):
        print("测试方法2")
        assert 2 != 1
        # self.assertIn('2', 'hello')

    @classmethod
    def tearDownClass(cls):
        print("这是整个类后要运行的方法")


if __name__ == '__main__':
    unittest.main(verbosity=2)
