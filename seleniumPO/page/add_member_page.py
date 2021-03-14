# 添加联系人的PO
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.seleniumPO.page.base_page import BasePage


class AddMemberPage(BasePage):

    # 参数化，通过传入参数，把要添加联系人的数据放在测试用例中
    def add_member(self, username, account, phonenum):
        '''
        添加联系人
        :return:
        '''
        # 输入 [姓名]
        self.driver.find_element(By.ID, 'username').send_keys(username)
        # 输入 [账号]
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        # 输入 [手机号]
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(phonenum)
        # 点击 [保存],当页面有多个相同的元素时，首先找到的是第一个
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        '''
        获取已添加的联系人
        :return:
        '''
        # 显示等待
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        # find_elements 查找页面上相同属性的元素，[element1,element2……]
        eles_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(eles_list)
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))

        return names
