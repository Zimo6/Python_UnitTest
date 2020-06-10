import unittest
from demo.UnitTest import forTest
from HTMLTestRunner import HTMLTestRunner
import os

#创建一个测试套件（可以理解为一个list）
suite = unittest.TestSuite()

#添加测试用例（子元素）到测试套件（list）
# 第一种方式
# suite.addTest(forTest('test_a'))
# suite.addTest(forTest('test_b'))
# suite.addTest(forTest('test_c'))
# 第二种方式
# case = [forTest('test_a'),forTest('test_a'),forTest('test_a')]
# suite.addTests(case)

# 第三种方式
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='UnitTes*.py')

# 第四种方式
# 运行某一个类下所有测试用例
suite.addTests(unittest.TestLoader().loadTestsFromName('demo.UnitTest.forTest'))
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(forTest))


#套件通过TextTestRunner运行器进行运行 约等于 unnittest.main（）
runner = unittest.TextTestRunner()
runner.run(suite)