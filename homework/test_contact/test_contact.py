from selenium.webdriver.remote.webdriver import WebDriver

from web.homework.page.main_page import MainPage

# --测试用例--
class TestContact():

    def setup(self):
        self.mainpage = MainPage()

    def test_contact(self):
        username = "aaa_15"
        account = "aaa_15"
        phonenum = "18918290015"

        page = self.mainpage.goto_add_member()

        page.add_member(username, account, phonenum)
        names = page.get_member()
        print(names)
        assert username in names
