import logging, os
from conf.read_conf import ReadConf

log_path = os.path.join(os.path.dirname(__file__), 'log_file/log.log')


class PrintLogInfo:
    def __init__(self, log_path=log_path):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        self.log_file = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.log_file.setFormatter(formatter)
        self.logger.addHandler(self.log_file)
        self.log_conscel = logging.StreamHandler()
        self.log_conscel.setFormatter(formatter)
        self.logger.addHandler(self.log_conscel)

    def log_info(self, message):
        self.logger.info(message)

    def err_info(self, message):
        self.logger.error(message)


logger = PrintLogInfo()
if __name__ == '__main__':
    # logger1 = LoggerInfo()
    logger.log_info('sss')
