"""
    目标：导入登陆业务实现层
"""

# 导包 unittest ApiLogin
import unittest
from api.api_res import ApiRes
from parameterized import parameterized
from tools.read_json_more import ReadJson


# 读取数据函数
def get_data():
    data = ReadJson("login_more.json").read_json()
    airs = []
    # 使用遍历获取所有value
    for data in data.values():
        airs.append((data.get("path"),
                     data.get("data"),
                     data.get("msg"),
                     data.get("status_code")
                     ))
    return airs


# 新建测试类
class TestLogin(unittest.TestCase):
    """批量登陆"""

    # 新建测试方法
    @parameterized.expand(get_data())
    # 传参顺序应和上面保持一致
    def test_login(self, path, data, msg, status_code):
        res = ApiRes().api_post(path, data)
        print("查看响应信息", res.json())

        # 断言响应信息
        self.assertEqual(msg, res.json()["msg"])

        # # 断言响应状态码
        self.assertEqual(status_code, res.status_code)


if __name__ == "__main__":
    unittest.main()
