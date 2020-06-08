import unittest

# 通过继承unittest.TestCase，来实现用例
class forTest(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        print('class')
    # 类的释放
    @classmethod
    def tearDownClass(cls) -> None:
        print('tclass')

    # 用例的初始化
    def setUp(self) -> None:
        print('setUP')
    # 用例的释放
    def tearDown(self) -> None:
        print('tearDown')

    # 普通函数(不会自动被识别)
    def plus(self, a, b):
        print(f'{a+b}={a}+{b}')

    # 测试用例
    def test_a(self):
        print('a')
    def test_b(self):
        print('b')
    def test_c(self):#调用普通函数
        self.plus(1, 2)

if __name__ == '__main__':
    unittest.main()