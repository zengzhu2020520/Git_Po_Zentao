import unittest, os, time
import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from action.login_in import Alawys_Action
from log.log_function import logger
from common.selenium_base_case import SeleniumBaseCase

report_path = os.path.join(os.path.dirname(__file__), '../../report/report_%s.html') % (time.strftime('%Y%m%d_%H%M%S'))


class Login_Test(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()
        # self.base_page.wait()
        # self.base_page.close_brower()

    def test_login_success(self):
        action = Alawys_Action(self.driver)
        main = action.login_success()
        actual_reesult = main.get_myusername()
        self.assertEqual(actual_reesult, '测试人员2', 'test_login_success用例执行失败')

    def test_login_faild(self):
        action_01 = Alawys_Action(self.driver)
        action_alter = action_01.login_failed(self.driver)
        print('actual:%s' % action_alter)
        self.assertEqual(action_alter, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_faild执行失败')


if __name__ == '__main__':
    unittest.main()
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(Login_Test('test_login_success'))
    # test_suite.addTest(Login_Test('test_login_faild'))
    # with open(report_path, 'w', encoding='utf-8') as file:
    #     http_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='测试报告', description='测试描述')
    #     http_runner.run(test_suite)
