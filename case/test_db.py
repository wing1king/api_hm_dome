# """
# 目标：在unittest框架中使用数据库工具类
# """
#
# # 导包 unittest测试工具类
# import unittest
# from tools.read_db import ReadDB
#
#
# # 新建测试类继承
# class TestDB(unittest.TestCase):
#     # 存新建测试方法
#     def test_db(self):
#
#         # 定叉sq1语句
#         sql = "select * from xingming where id = 6"
#
#         # 调用get_sql_one方法
#         data = ReadDB().get_sql_one(sql)
#         print("打印查到数据", data)
#
#         # 断言
#         self.assertEquals(6, data[1])
#
#
# if __name__ == '__main__':
#     unittest.main()