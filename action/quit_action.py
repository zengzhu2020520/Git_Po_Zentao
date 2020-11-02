import time
from main_function.main_page.main import MainPage
from main_function.login_page.login import LoginPage
from action.login_in import Alawys_Action


class QiutLogin:
    def __init__(self):
        self.action = Alawys_Action()
        self.action.login()
        self.driver = self.action.driver
        self.main_page = MainPage(self.driver)

    def quit(self):
        self.main_page.click_myusername()
        time.sleep(5)
        self.main_page.click_quit_button()
        # return LoginPage


if __name__ == '__main__':
    QiutLogin().quit()

