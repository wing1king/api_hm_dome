# """对着加
# 目标：自动化测试中操作项目数据库
# """
#
# # 导包pymysq1
# import pymysql
# # 存获取连接对象
# conn = pymysql.connect("127.0.0.1",
#                        "root",
#                        "123456",
#                        "test",
#                        charset="utf8"
#                        )
#
# # 获取游标对象
# cursor = conn.cursor()
# # 执行sql
# sql = "select * from xingming where id = 6"
# cursor.execute(sql)
# # 获取结果并进行断言
# res = cursor.fetchone()
# print(res)
# assert 6 == res[1]
#
# # 关闭游标对象
# cursor.close()
# # 关闭连接对象
# conn.close()