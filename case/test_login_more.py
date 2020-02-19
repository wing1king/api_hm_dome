"""
    目标：导入登陆业务实现层
"""

# 导包 unittest ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson


# 读取数据函数
def get_data():
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    # 使用遍历获取所有value
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("openid"),
                     data.get("uid"),
                     data.get("sessionid"),
                     data.get("msg"),
                     data.get("status_code")
                     ))
    return arrs


# 新建测试类
class TestLogin(unittest.TestCase):

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, url, openid, uid, sessionid, msg, status_code):
        res = ApiLogin().api_post_login(url, openid, uid, sessionid)
        print("查看响应信息", res.json())

        # 断言响应信息
        self.assertEquals(msg, res.json()["msg"])
        #
        # # 断言响应状态码
        self.assertEquals(status_code, res.status_code)


if __name__ == "__main__":
    unittest.main()
