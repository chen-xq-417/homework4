from selenium import webdriver
from selenium.webdriver.common.by import By

from web.homework.page.base_page import BasePage


# 添加 联系人页面的PO
class AddMemberPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def add_member(self, username, account, phonenum):
        # 输入 姓名
        self.driver.find_element(By.ID, "username").send_keys(username)
        # 输入 账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入 手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 点击 保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        eles_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(eles_list)
        names = []
        for name in eles_list:
            names.append(name.get_attribute("title"))

        print(names)
        return names
