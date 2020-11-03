import unittest, os, time
import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from action.login_in import Alawys_Action
from log.log_function import logger
from common.selenium_base_case import SeleniumBaseCase
from testcases.test_data_utils import TestDataUtils
from conf.read_conf import read_conf

report_path = os.path.join(os.path.dirname(__file__), '../../report/report_%s.html') % (time.strftime('%Y%m%d_%H%M%S'))
execl_path = os.path.join(os.path.dirname(__file__), '../../date/login_page.xlsx')


class Login_Test(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.test_date = TestDataUtils('login_suite', 'Login_Test', execl_path)
        self.data_infos = self.test_date.change_excel_data()

    def tearDown(self) -> None:
        super().tearDown()
        # self.base_page.wait()
        # self.base_page.close_brower()

    def test_login_success(self):
        test_login_success = self.data_infos['test_login_success']
        self._testMethodDoc = test_login_success['test_name']
        action = Alawys_Action(self.driver)
        main = action.login_success(username=test_login_success['test_parameter']['username'],
                                    password=test_login_success['test_parameter']['password'])
        actual_reesult = main.get_myusername()
        self.assertEqual(actual_reesult, test_login_success['excepted_reslt'], test_login_success['fail_message'])

    def test_login_faild(self):
        test_login_faild = self.data_infos['test_login_faild']
        action_01 = Alawys_Action(self.driver)
        action_alter = action_01.login_failed(username=test_login_faild['test_parameter']['username'],
                                              password=test_login_faild['test_parameter']['password'])
        print('actual:%s' % action_alter)
        self.assertEqual(action_alter, test_login_faild['excepted_reslt'], test_login_faild['fail_message'])


if __name__ == '__main__':
    unittest.main()
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(Login_Test('test_login_success'))
    # test_suite.addTest(Login_Test('test_login_faild'))
    # with open(report_path, 'w', encoding='utf-8') as file:
    #     http_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='测试报告', description='测试描述')
    #     http_runner.run(test_suite)
