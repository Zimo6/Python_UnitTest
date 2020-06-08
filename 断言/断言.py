#coding:utf-8
import unittest
from ddt import ddt,data,unpack,file_data

import yaml
# 需要导PyYAML库***********************


@ddt    #数据驱动
class forTestTest(unittest.TestCase):

    # 直接读取文件
    @file_data('date.yml')
    def test_1(self, **txt):
        name = txt.get('name')
        print(name)
        # 断言
        # self.assertEqual(name, '阿崔', msg='不是 阿崔')
        self.assertNotEqual(name, '阿崔', msg='是 阿崔')

        print(txt.get('info'))
        print('****************')

if __name__ == '__main__':
    unittest.main()