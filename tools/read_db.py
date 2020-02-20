"""
    目标：完成数据库相关工具类封装
    分析：
        1.主要方法
            假设：def get_sq1_one（sq1）
        2.辅助方法
            1.获取连接对象
            2.获取游标对象
            3.关闭游标对象方法
            4.关闭连接对象方法
"""

# 导包pymysq1
import pymysql


# 新建工具类数据库
class ReadDB:
    # 定义连接对象 类方法
    conn = None

    # 存获取连对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("127.0.0.1",
                                        "root",
                                        "123456",
                                        "test",
                                        charset="utf8"
                                        )

        return self.conn

    # 获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象方法封装
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭游标对象方法封装
    def close_conn(self):
        if self.conn:
            self.conn.close()
            # 注意：关闭连接对象后，对象还存在内存中，需要手工设置为None
            self.conn = None

    # 主要执行方法->在外界调用次方法就可以完成数据相应的操作def get_sql_one（self，sql）：passl
    def get_sql_one(self, sql):

        # 定义游标对象及数据变量
        sensor = None
        data = None
        try:
            # 获取游标对象
            sensor = self.get_cursor()

            # 调用执行方法
            sensor.execute(sql)

            # 获取结果
            data = sensor.fetchone()
        except Exception as e:
            print("gat_sql_one error", e)
        # 关闭游标对象
        finally:
            self.close_cursor(sensor)

            # 关闭连接对象
            self.close_conn()

            # 返回热行结果
            return data

    def get_sql_all(self, sql):

        # 定义游标对象及数据变量
        sensor = None
        data = None
        try:
            # 获取游标对象
            sensor = self.get_cursor()

            # 调用执行方法
            sensor.execute(sql)

            # 获取结果
            data = sensor.fetchall()
        except Exception as e:
            print("gat_sql_one error", e)
        # 关闭游标对象
        finally:
            self.close_cursor(sensor)

            # 关闭连接对象
            self.close_conn()

            # 返回热行结果
            return data

    def update_sql(self, sql):

        # 定义游标对象及数据变量
        sensor = None
        data = None
        try:
            # 获取游标对象
            sensor = self.get_cursor()

            # 调用执行方法
            sensor.execute(sql)

            # 提交事务
            self.conn.commit()

        except Exception as e:

            # 事务回滚
            self.conn.rollback()
            print("gat_sql_one error", e)
        # 关闭游标对象
        finally:
            self.close_cursor(sensor)

            # 关闭连接对象
            self.close_conn()
