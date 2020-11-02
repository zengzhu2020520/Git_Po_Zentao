import os
from selenium import webdriver
from conf.read_conf import ReadConf

conf_driver_path = ReadConf().get_conf_driver_path()
driver_path = os.path.join(os.path.dirname(__file__), '..', conf_driver_path)


class GetBrower:
    def __init__(self, driver_name='chrome', driver_path1=driver_path):
        self.driver_name = driver_name
        self.driver_path1 = driver_path1

    def get_brower_driver(self):
        if self.driver_name == 'chrome':
            driver = self.__get_chrome_driver()
            return driver

    def __get_chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument('–disable-gpu')  # 添加启动参数 (add_argument)  加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置编码格式 默认为utf-8
        chrome_driver_path = os.path.join(self.driver_path1, 'chromedriver.exe')
        chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        return chrome_driver


if __name__ == '__main__':
    driver = GetBrower().get_brower_driver()
    url = ReadConf().get_conf_URL_path()
    driver.get(url)
