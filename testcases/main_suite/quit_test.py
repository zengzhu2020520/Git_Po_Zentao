import unittest, time
from selenium.webdriver.support import expected_conditions as EC
from action.quit_action import QiutLogin
from common.selenium_base_case import SeleniumBaseCase
from action.login_in import Alawys_Action


class QuitBrower(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.quit_brower = QiutLogin(self.driver)
        # self.driver = self.quit_brower.driver
        # self.base_page = BasePage(self.driver)

    def tearDown(self) -> None:
        # time.sleep(5)
        # self.base_page.close_brower()
        super().tearDown()

    def test_quit_brower(self):
        action = Alawys_Action(self.driver)
        action.login()
        self.quit_brower.quit()
        actal_result = self.driver.title
        print(actal_result)
        self.assertEqual(actal_result.__contains__('用户登录'), True, 'test_quit_brower用例不通过')


if __name__ == '__main__':
    unittest.main()
