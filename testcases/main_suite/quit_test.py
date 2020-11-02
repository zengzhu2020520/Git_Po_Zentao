import unittest, time
from selenium.webdriver.support import expected_conditions as EC
from action.login_in import Alawys_Action
from action.quit_action import QiutLogin
from common.base_page import BasePage


# from common.base_page import BasePage
class QuitBrower(unittest.TestCase):
    def setUp(self) -> None:
        self.quit_brower = QiutLogin()
        self.driver = self.quit_brower.driver
        self.base_page = BasePage(self.driver)

    def tearDown(self) -> None:
        time.sleep(5)
        self.base_page.close_brower()

    def test_quit_brower(self):
        self.quit_brower.quit()
        actal_result = self.driver.title
        print(actal_result)
        self.assertEqual(actal_result.__contains__('用户登录'), True, 'test_quit_brower用例不通过')


if __name__ == '__main__':
    unittest.main()
