"""运行入口层

目标：
    1.搜索组装测试套件
    2.运行测套件并生成测试报告
"""
import unittest
import time
import tools.read_email
import os
from tools.HTMLTestRunner import HTMLTestRunner

# 第一步1；组装测试套件
suite = unittest.defaultTestLoader.discover("./case", pattern="test*.py")
# 第二步： 指定报告存放路径及文件名称
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 第三步： 运行测试套件并生成报告
with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)


# 发送邮件
# time.sleep(60)
#
# work_path = "/api_hm_dome/report"
# # 判断是否生成测试报告
# if not os.listdir(work_path):
#     print("还未生成测试报告")
# else:
#     email = tools.read_email.send_eamil()
#     print(email)


# import sys
# import time
# import unittest
# from imp import reload
# from HTMLTestRunner import HTMLTestRunner
# reload(sys)
#
#
# # 定义测试用例的目录为当前目录
# test_dir = 'D:\\apiAutoTestHmtt\\case'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
#
# if __name__ == "__main__":
#     # 按照一定的格式获取当前的时间
#     now = time.strftime("%Y-%m-%d %H-%M-%S")
#
#     # 定义报告存放路径
#     filename = r'D:\apiAutoTestHmtt\report\\' + now + '_test_teacher_result.html'
#
#     fp = open(filename, "wb")
#     # 定义测试报告
#     runner = HTMLTestRunner(stream=fp,
#                             title="平台接口测试报告",
#                             description="测试用例执行情况：")
#     # 运行测试
#     runner.run(discover)
#     # 关闭报告文件
#     fp.close()