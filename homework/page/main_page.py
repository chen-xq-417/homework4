from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# from selenium import  webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage():

    def __init__(self):
        self.driver = WebDriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def goto_add_member(self):
        # 点击添加联系人
        self.driver.fund_element(By.CSS_SELECTOR, ".")
