# -*- coding: utf-8 -*-
"""
@FileName：Selenium_demo.py
@Description：Selenium的demo演示
@Author：Ken
@Time：2021/6/15 22:55
"""
from time import sleep

from selenium import webdriver

drive = webdriver.Chrome()
drive.get("http://www.baidu.com")
drive.find_element_by_id('kw').send_keys('hello world')
drive.find_element_by_id('su').click()
sleep(3)
drive.quit()
