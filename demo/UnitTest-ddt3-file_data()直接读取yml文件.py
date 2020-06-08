#coding:utf-8
import unittest
from selenium import webdriver
import  time
from ddt import ddt,data,unpack,file_data

import yaml
# 需要导PyYAML库***********************


@ddt    #数据驱动
class forTestTest(unittest.TestCase):

    # 直接读取文件
    @file_data('cui.yml')
    def test_1(self, txt):
        print(txt)
        print('****************')

if __name__ == '__main__':
    unittest.main()