# from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# 封装基类
class BasePage:
    base_url = ""

    # 默认参数是一个=
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 复用打开的浏览器
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)
