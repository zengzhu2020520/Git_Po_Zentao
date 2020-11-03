#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: test_data_utils.py
# @time: 2020-11-3 17:02
# @desc:
import os
from common.ReadExcel_fengzhuang import ReadExcel_FengZhuang
from conf.read_conf import read_conf

execl_path = os.path.join(os.path.dirname(__file__), '..', read_conf.get_conf_execl_path())


class TestDataUtils:
    def __init__(self, test_suite_name, test_class_name, excel_path=execl_path):
        self.test_suite_name = test_suite_name
        self.test_class_name = test_class_name
        self.excel_path = excel_path
        self.read_excel_data_info = ReadExcel_FengZhuang(self.excel_path, self.test_suite_name)

    def change_excel_data(self):
        excel_data = self.read_excel_data_info.read_excel_fengzhuang()
        data_01 = {}
        for i in range(len(excel_data)):
            data_02 = {}
            data_03 = {}
            test_parameter = {}
            if excel_data[i][2] == self.test_class_name:
                data_02['test_name'] = excel_data[i][1]
                data_02['isnot'] = excel_data[i][3]
                data_02['excepted_reslt'] = excel_data[i][4]
                data_02['fail_message'] = excel_data[i][5]
                for j in range(6, len(excel_data[i])):
                    if len(excel_data[i][j]) > 2 and excel_data[i][j].__contains__('='):
                        data = excel_data[i][j].split('=')
                        test_parameter[data[0]] = data[1]
                data_02['test_parameter'] = test_parameter
            data_01[excel_data[i][0]] = data_02
        return data_01


if __name__ == '__main__':
    testdate = TestDataUtils('login_suite', 'Login_Test', execl_path)
    value = testdate.change_excel_data()
    print(value)
