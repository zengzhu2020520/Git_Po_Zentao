import time
from main_function.login_page.login import LoginPage
from common.get_brower_driver import GetBrower
from common.read_excel import ReadExcel
from conf.read_conf import read_conf
from log.log_function import logger


class MainPage(object):
    def __init__(self):
        # 把界面的控件元素作为属性
        self.login_page = LoginPage(GetBrower().get_brower_driver())
        self.driver = self.login_page.driver
        self.login_page.open_url(read_conf.get_conf_URL_path())
        self.login_page.input_username('test01')
        self.login_page.input_password('newdream123')
        self.login_page.click_login()
        elements = ReadExcel('main_page', 'main_page').read_execl_info()
        self.company_name = elements['company_name']
        self.product = elements['product']
        self.my_imfomation = elements['my_imfomation']
        self.my_dipan = elements['my_dipan']

    def get_company_name(self):  # 方法就是控件的操作
        ele = self.login_page.find_elements(self.company_name)
        get_company_name = ele.get_attribute('title')
        logger.log_info('成功获取公司名称%s' % get_company_name)
        return get_company_name

    def goto_mydipan(self):  # 进入我的地盘
        ele = self.login_page.find_elements(self.my_dipan)
        ele.click()
        logger.log_info('成功进入我的地盘')

    def goto_product(self):  # 进产品
        ele = self.login_page.find_elements(self.product)
        ele.click()
        logger.log_info('成功进入产品界面')

    def get_myusername(self):
        ele = self.login_page.find_elements(self.my_imfomation)
        get_username = ele.text
        return get_username


if __name__ == '__main__':
    # driver = BasePage().driver
    mainpage = MainPage()
    company_name = mainpage.get_company_name()
    print(company_name)
    mainpage.goto_product()
    time.sleep(3)
    print(mainpage.get_myusername())
    time.sleep(3)
    mainpage.goto_mydipan()
