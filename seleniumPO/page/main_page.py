from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from web.seleniumPO.page.add_member_page import AddMemberPage

# 首页的PO
from web.seleniumPO.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_addmember(self):
        '''
        首页
        :return:
        '''
        # 点击 添加联系人
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 跳转至 添加联系人页面
        return AddMemberPage(self.driver)
