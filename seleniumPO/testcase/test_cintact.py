from web.seleniumPO.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    # def teardown(self):
    #     self.mainpage.quit_driver()

    def test_addmember(self):
        username = 'aaa_09'
        account = 'aaa_09'
        phonenum = '18918290008'
        page = self.mainpage.goto_addmember()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        print(names)
        assert username in names
