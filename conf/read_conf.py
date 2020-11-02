import configparser, os

conf_file_path = os.path.join(os.path.dirname(__file__), '../conf/config.ini')


class ReadConf:
    def __init__(self, conf_path=conf_file_path):
        self.conf_path = conf_path
        self.conf = configparser.ConfigParser()
        self.conf.read(conf_path, encoding='utf-8')

    def __get_conf_value(self, sec, option):
        value = self.conf.get(sec, option)
        return value

    def get_conf_driver_path(self):
        return self.__get_conf_value('default', 'driver_path')

    def get_conf_driver_name(self):
        return self.__get_conf_value('default', 'driver_name')

    def get_conf_URL_path(self):
        return self.__get_conf_value('default', 'open_url')

    def get_conf_timeout(self):
        return self.__get_conf_value('default', 'time_out')

    def get_conf_scream_hot_path(self):
        return self.__get_conf_value('default', 'scream_hot_path')

    def get_conf_log_path(self):
        return self.__get_conf_value('default', 'log_path')

    def get_conf_username(self):
        return self.__get_conf_value('default', 'username')

    def get_conf_password(self):
        return self.__get_conf_value('default', 'password')


read_conf = ReadConf()
if __name__ == '__main__':
    print(ReadConf().get_conf_driver_name)
