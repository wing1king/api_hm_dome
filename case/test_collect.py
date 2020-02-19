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
    datas = ReadJson("collect_more.json").read_json()
    arrs = []
    # 使用遍历获取所有value
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("book_id"),
                     data.get("type"),
                     data.get("msg"),
                     data.get("status_code")
                     ))
    return arrs


# 新建测试类
class TestLogin(unittest.TestCase):

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, url, book_id, type, msg, status_code):
        res = ApiCollect().api_post_collect(url, book_id, type)
        print("查看响应信息", res.json())

        # 断言响应信息
        self.assertEqual(msg, res.json()["msg"])
        #
        # # 断言响应状态码
        self.assertEqual(status_code, res.status_code)


if __name__ == "__main__":
    unittest.main()
