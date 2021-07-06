# -*- coding: utf-8 -*-
"""
@FileName：Element_locate_demo.py
@Description：
@Author：Ken
@Time：2021/6/18 22:45

--作业
1. 实现web端网易云的基于QQ登录的自动化操作
2. 将网易云的元素定位都统一使用xpath，并且手写来实现。
http://music.163.com

//*[@id="auto-id-MX8lzT8DDoii0JKU"]/a
"""
from time import sleep

from selenium import webdriver

# 创建webdriver
drive = webdriver.Chrome()
# 访问URL
drive.get("http://music.163.com")
drive.maximize_window()  # 窗体最大化
sleep(2)  # 等待2S，等待能使代码运行成功率更高
drive.find_element('xpath', '//a[contains(@data-action,"login")]').click()
drive.find_element('xpath', '//a[@data-action="switch"]').click()
drive.find_element('xpath', '//input[@type="checkbox"]').click()
sleep(2)
drive.find_element('xpath', '//i[@class="u-mlg2 u-mlg2-qq"]').click()
sleep(4)
all_handles = drive.window_handles
drive.switch_to.window(all_handles[-1])
sleep(5)
drive.find_element('xpath', '//a[@id="switcher_plogin"]').click()
# sleep(3)
# drive.find_element('xpath', '//i[@class="icn icn-ex"]').click()
# sleep(3)
drive.quit()
