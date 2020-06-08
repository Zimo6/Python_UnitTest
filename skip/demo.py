#coding:utf-8
import unittest
from ddt import ddt, data, unpack
# 需要导入ddt库******************

@ddt    #数据驱动
class forTestTest(unittest.TestCase):

    #无条件跳过执行该条用例
    @unittest.skip('理由就是不想运行')
    def test_1(self):
        print('1')

    #有条件执行跳过操作
    @unittest.skipIf(3 < 2,'这是if的理由（前面为假才会执行用例）')
    def test_2(self):
        print('2')

    # 有条件执行跳过操作
    @unittest.skipUnless(1 < 2, '这是unless的理由（前面为真才会执行用例）')
    def test_3(self):
        print('3')

    #如果用例执行失败，则不计入失败的case数
    @unittest.expectedFailure
    def test_4(self):
        print('4')
        self.assertEqual('4',4,msg='4不等于4')

    def test_5(self):
        print('5')
        self.assertEqual('5','haha',msg="5不等于haha")

if __name__ == '__main__':
    unittest.main()