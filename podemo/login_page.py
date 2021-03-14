from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


# 登录页面的PO
class LoginPage():
    # 定义一个init用来接收在index_pagez中loginpage的传参
    # driver:WebDriver,给driver指定一个类型，然后就可以使用WebDriver的一些方法
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        # 点击 注册链接
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        # 跳转 注册页面
        return RegisterPage(self.driver)
