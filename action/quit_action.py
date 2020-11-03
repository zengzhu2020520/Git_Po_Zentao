import time
from main_function.main_page.main import MainPage
from action.login_in import Alawys_Action
from common.get_brower_driver import GetBrower


class QiutLogin:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)

    def quit(self):
        self.main_page.click_myusername()
        time.sleep(5)
        self.main_page.click_quit_button()
        # return LoginPage


if __name__ == '__main__':
    action = Alawys_Action(GetBrower().get_brower_driver())
    driver = action.driver
    action.login()
    QiutLogin(driver).quit()
