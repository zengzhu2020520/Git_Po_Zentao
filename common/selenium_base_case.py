import unittest, time
from conf.read_conf import read_conf
from common.base_page import BasePage
from common.get_brower_driver import GetBrower


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = read_conf.get_conf_URL_path()

    def setUp(self) -> None:
        self.base_page = BasePage(GetBrower().get_brower_driver())
        self.driver = self.base_page.driver
        self.base_page.implicity_wait()
        self.base_page.open_url(self.url)
        return self.driver

    def tearDown(self) -> None:
        self.base_page.close_brower()

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
