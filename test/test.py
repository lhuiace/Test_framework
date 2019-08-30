import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, REPORT_PATH ,LOG_PATH
from utils.log import logger,logbug
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email


class TestBao(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        url = Config().get('URL')
        logger.info(url)
        logbug.info(111)

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='壁虎自动化测试报告', description='报告')
        runner.run(TestBao('test1'))
    f = open(report,'rb')
    mail_body = f.read()
    e = Email(title='自动化测试报告',
              message=mail_body,
              receiver='lianghao@91bihu.com',
              server='smtp.exmail.qq.com',
              sender='lianghao@91bihu.com',
              password='o84L5wCvByfkv7kV',
              path=report
              )
    e._attach_file(LOG_PATH+'\\'+'bug.log')
    e.send()
