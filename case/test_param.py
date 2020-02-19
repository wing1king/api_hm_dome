"""
    目标：回顾parameterized参数化组件使用安装：
    安装：
        pip install parameterized
    使用：
        @paramaterized（参数）
        参数：
            单个参数格式：列表如：[值1，值2】
            多个参数：列表嵌套元祖：如：f（参1值，参2值）]
    需求：
        输出用户名和密码，数据分别为1.admin，1234562.user002，654321
"""

# 导包
import unittest
from parameterized import parameterized


# 新建测试类
class TestPara(unittest.TestCase):

    # 存新建测试方法
    @parameterized.expand([("admin", "123456"), ("user002", "654321")])
    def test_para(self, username, password):
        print("用户名：", username)
        print("密码：", password)



