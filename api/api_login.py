"""
目标：实现登陆接口对象封装
"""

# 导包 requests
import requests


# 新建类  登陆接口对象
class ApiLogin(object):
    # 新建方法 登陆方法
    def api_post_login(self, url, openid, uid, sessionid):
        # headers 定义
        headers = {"Content-Type": "application/json"}
        # data 定义
        data = {"openid": openid, "uid": uid, "sessionid": sessionid}
        # 调用post并返回响应结果
        return requests.post(url, headers=headers, json=data)


"""
    提示：url、mobile、code：最后都需要从data数据文件读取出来，做参数化使用，所以这里我们动态传参剑
"""