from main_function.login_page.login import LoginPage
from common.get_brower_driver import GetBrower
from log.log_function import logger
from conf.read_conf import read_conf
from main_function.main_page.main import MainPage


class Alawys_Action:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = GetBrower().get_brower_driver()
        self.login_page = LoginPage(self.driver)
        # self.login_page.open_url(read_conf.get_conf_URL_path())
        # self.login_page.set_browner_max_windows()

    def login_success(self, username='test02', password='newdream123'):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()
        logger.log_info('成功登录')
        return MainPage(self.driver)

    def login_failed(self, username='test002', password='newdream123'):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()
        logger.err_info('用户名或者密码不正确')
        return self.login_page.get_alter_message()

    def login(self):
        self.login_page.input_username(read_conf.get_conf_username())
        self.login_page.input_password(read_conf.get_conf_password())
        self.login_page.click_login()
        logger.log_info('使用默认账号登录成功')
        return MainPage(self.driver)


if __name__ == '__main__':
    action = Alawys_Action(GetBrower().get_brower_driver())
    action.login_success()
