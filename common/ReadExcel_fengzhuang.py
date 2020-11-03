#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: ReadExcel_fengzhuang.py
# @time: 2020-11-3 12:42
# @desc:
import xlrd3, os

file_path = os.path.join(os.path.dirname(__file__), '../date/login_page.xlsx')


class ReadExcel_FengZhuang:
    '''判断是否是Excel文件在处理  XLS XLSX 并且存在'''

    def __init__(self, excel_path, sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        read_excel = xlrd3.open_workbook(self.excel_path)
        if self.sheet_name:
            self.sheet = read_excel.sheet_by_name(self.sheet_name)
        else:
            self.sheet = read_excel.sheet_by_index(0)

    def __get_sheet_rowws(self):
        return self.sheet.nrows

    def __get_sheet_ncols(self):
        return self.sheet.ncols

    def read_excel_fengzhuang(self):
        excel_date = []
        for i in range(1, self.__get_sheet_rowws()):
            date = []
            for j in range(self.__get_sheet_ncols()):
                value = self.sheet.cell_value(i, j)
                date.append(value)
            excel_date.append(date)
        return excel_date


if __name__ == "__main__":
    re = ReadExcel_FengZhuang(file_path,'main_page')
    date = re.read_excel_fengzhuang()
    print(date)
