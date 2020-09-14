import pymysql
from demo_api_auto.tools.project_path import *
from demo_api_auto.tools.read_config import ReadConfig


class DoMysql:
    conn = None

    def _get_conn(self):
        if self.conn is None:
            db_config = eval(ReadConfig().get_config(test_config_path, "DB", "db_config"))
            self.conn = pymysql.connect(**db_config, charset="utf8")
        return self.conn

    def _get_cursor(self):
        return self._get_conn().cursor()

    def _close_cursor(self, cursor):
        if self.cursor:
            cursor.close()

    def _close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None  # 关闭连接对象后，对象还存在内存中，需要手工设置为None

    def get_sql_one(self, sql):
        cursor = None
        data = None
        try:
            cursor = self._get_cursor()
            cursor.execute(sql)
            data = cursor.fetchone()  # 元组
        except Exception as e:
            print(e)
        finally:
            self._close_cursor(cursor)
            self._close_conn()
            return data

    def get_sql_all(self, sql):
        cursor = None
        data = None
        try:
            cursor = self._get_cursor()
            cursor.execute(sql)
            data = cursor.fetchall()  # 列表嵌套元组
        except Exception as e:
            print(e)
        finally:
            self._close_cursor(cursor)
            self._close_conn()
            return data

    def update_sql(self, sql):
        cursor = None
        try:
            cursor = self._get_cursor()
            cursor.execute(sql)
            self.conn.commit()  # 事务提交
        except Exception as e:
            self.conn.rollback()  # 事务回滚
            print(e)
        finally:
            self._close_cursor(cursor)
            self._close_conn()
