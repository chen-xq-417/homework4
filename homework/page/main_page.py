from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from web.homework.page.add_member_page import AddMemberPage
from web.homework.page.base_page import BasePage


# 主页的PO
class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    # def __init__(self):
    #     # 复用打开的浏览器
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    #     self.driver.implicitly_wait(5)

    def goto_add_member(self):
        # 点击 添加联系人
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 跳转至 添加联系人页面
        return AddMemberPage(self.driver)
