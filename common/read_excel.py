import xlrd3, os

data_path = os.path.join(os.path.dirname(__file__), '../date/login_page.xlsx')


class ReadExcel:
    def __init__(self, model_name, page_name, date_path1=data_path):
        self.date_path1 = date_path1
        self.model_name = model_name
        self.page_name = page_name
        self.read_execl = xlrd3.open_workbook(date_path1)
        self.sheet = self.read_execl.sheet_by_name(page_name)

    def read_execl_info(self):
        date_list = {}
        for i in range(1, self.sheet.nrows):
            if self.sheet.cell_value(i, 2) == self.model_name:
                date_date_list = {'elemen_name': self.sheet.cell_value(i, 1),
                                  'page_belong': self.sheet.cell_value(i, 2),
                                  'locate_type': self.sheet.cell_value(i, 3),
                                  'locate_value': self.sheet.cell_value(i, 4),
                                  'time_out': self.sheet.cell_value(i, 5) if isinstance(self.sheet.cell_value(i, 5),
                                                                                        float) else float(5)}
                date_list[self.sheet.cell_value(i, 0)] = date_date_list
        return date_list


if __name__ == '__main__':
    readexcel = ReadExcel('login_page', 'login_page')
    values =readexcel.read_execl_info()
    for i in values.values():
        print(i)
