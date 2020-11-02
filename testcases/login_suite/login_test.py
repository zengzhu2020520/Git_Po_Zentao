import unittest, os, time
import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.get_brower_driver import GetBrower
from common.base_page import BasePage
from action.login_in import Alawys_Action
from conf.read_conf import read_conf
from log.log_function import logger

report_path = os.path.join(os.path.dirname(__file__), '../../report/report_%s.html') % (time.strftime('%Y%m%d_%H%M%S'))


class Login_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.action = Alawys_Action()
        self.driver = self.action.driver
        self.base_page = BasePage(self.driver)

    def tearDown(self) -> None:
        self.base_page.wait()
        self.base_page.close_brower()

    def test_login_success(self):
        self.action.login_success()
        self.assertTrue(WebDriverWait(self.driver, 5).until(
            EC.title_contains('禅道')), '登录失败')

    def test_login_faild(self):
        self.action.login_failed()
        self.assertTrue(WebDriverWait(self.driver, 5).until(EC.alert_is_present()),
                        '测试用例失败，没有弹窗')
        alter = self.driver.switch_to.alert
        print(alter.text)
        logger.err_info('登录失败，失败原因为：%s' % alter.text)


if __name__ == '__main__':
    # unittest.main()
    test_suite = unittest.TestSuite()
    test_suite.addTest(Login_Test('test_login_success'))
    test_suite.addTest(Login_Test('test_login_faild'))
    with open(report_path, 'w', encoding='utf-8') as file:
        http_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='测试报告', description='测试描述')
        http_runner.run(test_suite)
