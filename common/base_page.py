import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.read_conf import read_conf
from log.log_function import PrintLogInfo
from log.log_function import logger
from common.get_brower_driver import GetBrower

url_path = read_conf.get_conf_URL_path()
time_out_conf = read_conf.get_conf_timeout()
scream_hot_file_path = os.path.join(os.path.dirname(__file__), '../scream_hot',
                                    'scream_hot_%s.png' % (time.strftime('%Y%m%d_%H%M%S')))


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(time_out_conf)

    def open_url(self, url=url_path):
        self.driver.get(url)

    def close_current_page(self):
        self.driver.close()

    def close_brower(self):
        self.driver.quit()


    def set_browner_max_windows(self):
        self.driver.maximize_window()

    def set_browner_min_windows(self):
        self.driver.minimize_window()

    def implicity_wait(self, time_out=5):
        self.driver.implicitly_wait(time_out)

    def wait(self, time_out=5):
        time.sleep(time_out)

    def find_elements(self, ele_infos):
        ele_locate_type = ele_infos['locate_type']
        ele_locate_value = ele_infos['locate_value']
        ele_time_out = ele_infos['time_out']
        if ele_locate_type == 'id':
            locate_type = By.ID
        elif ele_locate_type == 'xpath':
            locate_type = By.XPATH
        elif ele_locate_type == 'name':
            locate_type = By.NAME
        elif ele_locate_type == 'class':
            locate_type = By.CSS_SELECTOR
        element = WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(locate_type, ele_locate_value))
        if element:
            logger.log_info('元素%s定位成功' % ele_infos['elemen_name'])
        return element

    def click(self, ele_infos):
        ele = self.find_elements(ele_infos)
        ele.click()
        logger.log_info('成功点击%s这个元素' % ele_infos['elemen_name'])

    def input(self, ele_info, conent):
        input_ele = self.find_elements(ele_info)
        input_ele.send_keys(conent)
        logger.log_info('%s输入成功' % ele_info['elemen_name'])

    # 框架跳转
    def switchFranme(self, ele_info):
        ele = self.find_elements(ele_info)
        self.driver.swith_to.frame(ele)

    def switchFrane1(self, **element_dict):
        if 'id' in element_dict.keys():
            self.driver.swith_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.swith_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            ele = self.find_elements(element_dict['element'])
            self.driver.swith_to.frame(ele)

    # 鼠标键盘封装（建议代码思路：判断操作系统类型）
    def move_to_actionchains(self, ele_info):
        element = self.find_elements(ele_info)
        ActionChains(self.driver).move_to_element(element)

    def long_press_elemnt(self, ele_info, senconds):
        element = self.find_elements(ele_info)
        ActionChains(self.driver).click_and_hold(element).pause(senconds).perform()

    # 弹出窗的封装
    def get_alter_message(self, time_ou=5, action='accept'):
        WebDriverWait(self.driver, time_ou).until(EC.alert_is_present())
        self.wait(5)
        alter = self.driver.swith_to.alter
        alter_test = alter.text
        if action == 'accept':
            alter.accept()
        else:
            alter.dismiss()
        return alter_test

    # 切换句柄的封装
    def switch_to_windows_by_title(self, title):
        self.driver = webdriver.Chrome()
        current_window_handle = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, time_out_conf).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_to_windows_by_url(self, url):
        self.driver = webdriver.Chrome()
        current_window_handle = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, time_out_conf).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    # 截图封装
    def scream_hot(self, photo_file=scream_hot_file_path):
        self.driver.get_screenshot_as_file(scream_hot_file_path)

    # 移除属性

    def remove_attibute(self, ele_info, remove_name):
        self.driver.execute_script('arguments[0].removeAttribute(%d)' % remove_name, ele_info)

    def set_attibute(self, set_name, set_vale, ele_info):
        self.driver.execute_script("arguments[0].setAttribute('%s','%s')'%(set_name,set_vale) ,ele_info")


if __name__ == '__main__':
    driver = GetBrower().get_brower_driver()
    base_page = BasePage(driver)
    base_page.open_url(read_conf.get_conf_URL_path())
    base_page.scream_hot()
