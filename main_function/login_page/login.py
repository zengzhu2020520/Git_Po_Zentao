from selenium import webdriver
from common.base_page import BasePage
from log.log_function import logger
from common.get_brower_driver import GetBrower
from common.read_excel import ReadExcel
from conf.read_conf import read_conf


class LoginPage(BasePage):
    def __init__(self, driver):
        # 把界面的控件元素作为属性
        super().__init__(driver)
        # self.username_inputbox = {'elemen_name': '用户输入框',
        #                           'locat_type': 'xpath',
        #                           'locate_value': '//input[@id="account"]',
        #                           'time_out': 2}
        # self.password_inputbox = {'elemen_name': '密码输入框',
        #                           'locat_type': 'xpath',
        #                           'locate_value': '//input[@name="password"]',
        #                           'time_out': 3}
        # self.login_button = {'elemen_name': '登录按钮',
        #                      'locat_type': 'xpath',
        #                      'locate_value': '//button[@id="submit"]',
        #                      'time_out': 4}
        self.driver = driver
        ele_info = ReadExcel('login_page', 'login_page').read_execl_info()
        self.username_inputbox = ele_info['username_inputbox']
        self.password_inputbox = ele_info['password_inputbox']
        self.login_button = ele_info['login_button']

    def input_username(self, username):  # 方法就是控件的操作
        self.input(self.username_inputbox, username)
        logger.log_info('正确输入用户名%s' % str(username))

    def input_password(self, password):
        self.input(self.password_inputbox, password)
        logger.log_info('正确输入用户名%s' % str(password))

    def clear_input_username(self, password):
        ele = self.find_elements(self.username_inputbox)
        ele.clear()

    def clear_input_password(self):
        ele = self.find_elements(self.password_inputbox)
        ele.clear()

    def click_login(self):
        self.click(self.login_button)
        logger.log_info('正确登录')


if __name__ == '__main__':
    driver = GetBrower().get_brower_driver()
    login_page = LoginPage(driver)
    login_page.open_url(read_conf.get_conf_URL_path())
    login_page.set_browner_max_windows()
    login_page.input_username('test02')
    login_page.input_password('newdream123')
    login_page.click_login()
    login_page.scream_hot()
