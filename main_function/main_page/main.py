import time
from common.base_page import BasePage
from common.get_brower_driver import GetBrower
from common.read_excel import ReadExcel
from conf.read_conf import read_conf
from log.log_function import logger


class MainPage(BasePage):
    def __init__(self, driver):
        # 把界面的控件元素作为属性
        super().__init__(driver)
        # self.driver = driver
        elements = ReadExcel('main_page', 'main_page').read_execl_info()
        self.company_name = elements['company_name']
        self.product = elements['product']
        self.my_imfomation = elements['my_imfomation']
        self.my_dipan = elements['my_dipan']
        self.quit_button = elements['quit_button']

    def get_company_name(self):  # 方法就是控件的操作
        ele = self.find_elements(self.company_name)
        get_company_name = ele.get_attribute('title')
        logger.log_info('成功获取公司名称%s' % get_company_name)
        return get_company_name

    def goto_mydipan(self):  # 进入我的地盘
        ele = self.find_elements(self.my_dipan)
        ele.click()
        logger.log_info('成功进入我的地盘')

    def goto_product(self):  # 进产品
        ele = self.find_elements(self.product)
        ele.click()
        logger.log_info('成功进入产品界面')

    def get_myusername(self):
        ele = self.find_elements(self.my_imfomation)
        get_username = ele.text
        return get_username

    def click_myusername(self):
        ele = self.find_elements(self.my_imfomation)
        ele.click()

    def click_quit_button(self):
        ele = self.find_elements(self.quit_button)
        ele.click()


if __name__ == '__main__':
    driver = GetBrower().get_brower_driver()
    mainpage = MainPage(driver)
    company_name = mainpage.get_company_name()
    print(company_name)
    mainpage.goto_product()
    time.sleep(3)
    print(mainpage.get_myusername())
    time.sleep(3)
    mainpage.goto_mydipan()
