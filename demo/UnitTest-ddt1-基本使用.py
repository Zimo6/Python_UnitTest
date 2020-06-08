#coding:utf-8
import unittest
from ddt import ddt, data, unpack
# 需要导入ddt库******************
def readFile():
    # 定义一个列表
    params= []
    # 以读取的形式打开参数文档
    file = open('param.txt','r',encoding='utf-8')
    for line in file.readlines():
        # 把读取的这一行前后的'回车'干掉，用逗号分隔
        # 第一次循环: 列表总添加元素为 ('小猫','小狗')
        params.append(line.strip('\n').split(','))
    file.close()
    return params

@ddt    #数据驱动
class forTestTest(unittest.TestCase):

    # 打印一个参数
    # @data('小猫','小狗')
    # def test_1(self,txt):
    #     print(txt)

    #打印两个参数
    # @data(('小猫', '小狗'), ('小牛','大牛'))
    # @unpack     #解包
    # def test_1(self, txt1, txt2):
    #     print(txt1)
    #     print(txt2)
    #     print('****************')

    # 配合文件使用
    @data(*readFile())  #一个*读取列表
    @unpack     #解包
    def test_1(self, txt1, txt2):
        print(txt1)
        print(txt2)
        print('****************')

if __name__ == '__main__':
    unittest.main()