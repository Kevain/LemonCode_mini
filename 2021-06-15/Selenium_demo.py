# -*- coding: utf-8 -*-
"""
@FileName：Selenium_demo.py
@Description：Selenium的demo演示
@Author：Ken
@Time：2021/6/15 22:55
"""
from time import sleep

from selenium import webdriver


# driver = webdriver.Chrome()
#
# driver.get('http://www.baidu.com')
# driver.maximize_window()
# sleep(1)
# # 通过id定位百度输入框，并输入'python'
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.quit()


# 封装
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_by_id(self):
        # 通过find_element_by_id定位
        self.driver.find_element_by_id('kw').send_keys('python')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_by_name(self):
        # 通过find_element_by_name定位
        self.driver.find_element_by_name('wd').send_keys('google')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_by_linktext(self):
        # 通过find_element_by_link_text定位
        self.driver.find_element_by_link_text('学术').click()
        # 切换句柄
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
        sleep(3)
        self.driver.quit()

    def test_by_patail_linktext(self):
        # 通过find_element_by_partial_link_text定位元素。取链接文本的一小部分
        self.driver.find_element_by_partial_link_text('全国').click()
        sleep(4)
        self.driver.quit()

    def test_xpath(self):
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys('xpath')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(3)
        self.driver.quit()

    def test_tag(self):
        # 通过find_elements_by_tag_name定位元素
        input = self.driver.find_elements_by_tag_name('input')[0]
        print(input)

    def test_by_css(self):
        # 通过find_element_by_css_selector定位
        self.driver.find_element_by_css_selector('#kw').send_keys('css')
        self.driver.find_element_by_css_selector('#su').click()
        sleep(2)
        self.driver.quit()

    def test_by_class(self):
        # 通过find_element_by_class_name定位元素
        self.driver.find_element_by_class_name('s_ipt').send_keys('class')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_all(self):
        self.driver.find_element(value='kw').send_keys('allelement')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    # TestCase().test_by_id()
    # TestCase().test_by_name()
    # TestCase().test_by_linktext()
    # TestCase().test_by_patail_linktext()
    # TestCase().test_xpath()
    # TestCase().test_tag()
    # TestCase().test_by_css()
    # TestCase().test_by_class()
    TestCase().test_all()
