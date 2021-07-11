# -*- coding: utf-8 -*-
"""
@FileName：util.py
@Description：
@Author：Ken
@Time：2021/7/6 21:14
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    sleep(2)

    get_element(driver, By.ID, 'kw').send_keys('selenium')
    get_element(driver, By.ID, 'su').click()
    sleep(2)
    driver.quit()
