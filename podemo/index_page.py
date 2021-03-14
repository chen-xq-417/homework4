from typing import Type

from selenium import webdriver
from selenium.webdriver.common.by import By
from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


# 首页的PO
class IndexPage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com")

    def goto_login(self):
        '''
        登录
        :return:
        '''
        # 点击 登录 按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        # 跳转至 登录页面,传参，在LoginPage中就可以只直接使用self.driver
        return LoginPage(self.driver)

    def goto_register(self):
        '''
        注册
        :return:
        '''
        # 点击 立即注册 按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        # 跳转至 注册页面
        return RegisterPage(self.driver)
