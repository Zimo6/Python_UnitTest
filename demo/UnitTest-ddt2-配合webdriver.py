#coding:utf-8
import unittest
from selenium import webdriver
import  time
from ddt import ddt,data,unpack

def readFile():
    # 定义一个列表
    params = []
    # 以读取的形式打开参数文档
    file = open('param-auto.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        # 把读取的这一行前后的 回车 干掉，用逗号分隔
        # 第一次循环: 列表总添加元素为 ('http://www.baidu.com','小狗')
        params.append(line.strip('\n').split(','))
    file.close()
    return params

@ddt    #数据驱动
class forTestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    # 配合文件使用
    @data(*readFile())  #一个*读取列表
    @unpack
    def test_1(self, url, txt):
        self.driver.get(url)
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main()