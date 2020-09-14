import unittest
from demo_api_auto.tools.http_request import HttpRequest
from ddt import ddt, data
from demo_api_auto.tools.do_excel import DoExcel
from demo_api_auto.tools.get_cookie import GetCookie
from demo_api_auto.tools.project_path import *
from demo_api_auto.tools.my_logger import MyLog
from demo_api_auto.tools.do_mysql import DoMysql

my_logger = MyLog()
test_data = DoExcel.get_data(test_case_path)


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUP(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        my_logger.info("开始执行用例{0}:{1}".format(item["case_id"], item["title"]))
        # if item["check_sql"] !=None:
        #     my_logger.info(f"此条用例需要做数据库校验:{item['check_sql']}")
        #     query_sql=eval(item["check_sql"]["sql"])
        #     before_query_sql=DoMysql().get_sql_one(query_sql)[0]
        #     my_logger.info(f"用例:{item['title']} 请求之前的数据是:{before_query_sql}")
        #     my_logger.info("------------开始http接口请求------------")
        #     res=HttpRequest.http_request(item["url"],eval(item["data"]),item["http_method"],getattr(GetCookie,"COOKIE"))
        #     my_logger.info("------------完成http接口请求------------")
        #     after_query_sql=DoMysql().get_sql_one(query_sql)[0]
        #     my_logger.info(f"用例:{item['title']} 请求之前的数据是:{after_query_sql}")
        my_logger.info("------------开始http接口请求------------")
        res = HttpRequest.http_request(item["url"], eval(item["data"]), item["http_method"],
                                       getattr(GetCookie, "COOKIE"))
        my_logger.info("------------完成http接口请求------------")

        if res.cookies:
            setattr(GetCookie, "COOKIE", res.cookies)
        try:
            self.assertEqual(str(item["expected"]), res.json()["code"])
            TestResult = "PASS"
        except AssertionError as e:
            TestResult = "Failed"
            my_logger.error(f"执行用例出错:{e}")
            raise e
        finally:
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"] + 1, str(res.json()), TestResult)
            my_logger.info(f"获取到的结果是:{res.json()}")
