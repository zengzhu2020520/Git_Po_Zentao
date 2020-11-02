from main_function.login_page.login import LoginPage
from common.get_brower_driver import GetBrower
from log.log_function import logger
from conf.read_conf import read_conf


class Alawys_Action:
    def __init__(self):
        # self.driver = GetBrower().get_brower_driver
        self.driver = GetBrower().get_brower_driver()
        self.login_page = LoginPage(self.driver)
        self.login_page.open_url(read_conf.get_conf_URL_path())

    def login_success(self, username='test02', password='newdream123'):
        self.login_page.input_username('test02')
        self.login_page.input_password('newdream123')
        self.login_page.click_login()
        logger.log_info('成功登录')

    def login_failed(self, username='test002', password='newdream123'):
        self.login_page.input_username('test002')
        self.login_page.input_password('newdream123')
        self.login_page.click_login()
        logger.err_info('用户名或者密码不正确')
        return self.login_page.get_alter_message()

    def login(self):
        self.login_page.input_username(read_conf.get_conf_username())
        self.login_page.input_password(read_conf.get_conf_password())
        self.login_page.click_login()
        logger.log_info('使用默认账号登录成功')


if __name__ == '__main__':
    action = Alawys_Action()
    action.login_success()
