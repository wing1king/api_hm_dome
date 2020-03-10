"""
    目标：导入登陆业务实现层
"""

# 导包 unittest ApiLogin
import unittest
from api.api_collect import ApiCollect
from parameterized import parameterized
from tools.read_json import ReadJson


# 读取数据函数
def get_data():
    data = ReadJson("collect_more.json").read_json()
    arrs = []
    # 使用遍历获取所有value
    arrs.append((data.get("path"),
                 data.get("data"),
                 data.get("msg"),
                 data.get("status_code")
                     ))
    return arrs


def get_qx_data():
    data = ReadJson("collect_more1.json").read_json()
    arrs = []
    # 使用遍历获取所有value
    arrs.append((data.get("path"),
                 data.get("data"),
                 data.get("msg"),
                 data.get("status_code")
                     ))
    return arrs


# 新建测试类
class TestCollect(unittest.TestCase):
    """收藏/取消收藏作品"""

    # 新建测试方法
    """收藏作品"""
    @parameterized.expand(get_data())
    def test01_collect(self, path, data, msg, status_code):

        res = ApiCollect.api_post(path, data)

        print("查看响应信息", res.json())

        # 断言响应信息
        self.assertEqual(msg, res.json()["msg"])

        # # 断言响应状态码
        self.assertEqual(status_code, res.status_code)

    """取消收藏作品"""
    @parameterized.expand(get_qx_data())
    def test02_collect(self, path, data, msg, status_code):

        res = ApiCollect.api_post(path, data)

        print("查看响应信息", res.json())

        # 断言响应信息
        self.assertEqual(msg, res.json()["msg"])

        # # 断言响应状态码
        self.assertEqual(status_code, res.status_code)


if __name__ == "__main__":
    unittest.main()
