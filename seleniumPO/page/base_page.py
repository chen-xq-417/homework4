from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 复用浏览器,需要设置 option.debugger_address
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            # 创建完driver，立刻设置隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)
