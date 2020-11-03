import unittest, time
from conf.read_conf import read_conf
from common.base_page import BasePage
from common.get_brower_driver import GetBrower
from log.log_function import logger


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.log_info('===============开始执行setupclass=============')
        cls.url = read_conf.get_conf_URL_path()

    def setUp(self) -> None:
        logger.log_info('===============开始执行测试用例=============')
        self.base_page = BasePage(GetBrower().get_brower_driver())
        self.driver = self.base_page.driver
        self.base_page.implicity_wait()
        try:
            self.base_page.open_url(self.url)
        except Exception as e:
            logger.err_info('打开浏览器失败，浏览器地址为：%s,%s' % (self.url, e.__str__()))
        return self.driver

    def tearDown(self) -> None:
        self.base_page.close_brower()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.log_info('===============用例执行完成=============')


if __name__ == '__main__':
    unittest.main()
