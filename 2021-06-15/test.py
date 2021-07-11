# -*- coding: utf-8 -*-
"""
@FileName：test.py
@Description：
@Author：Ken
@Time：2021/7/5 22:56
"""
from time import sleep

from selenium import webdriver


class TestElementOne():
    def __init__(self):
        self.drive = webdriver.Chrome()
        self.drive.get('https://www.baidu.com')
        self.drive.maximize_window()
        sleep(3)

    def test_by_id(self):
        self.drive.find_element_by_id('kw').send_keys('byid')
        self.drive.find_element_by_id('su').click()
        sleep(3)
        self.drive.quit()


if __name__ == '__main__':
    TestElementOne().test_by_id()
