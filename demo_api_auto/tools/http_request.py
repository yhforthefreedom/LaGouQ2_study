import requests
from demo_api_auto.tools.my_logger import MyLog

my_logger = MyLog()


class HttpRequest:
    @staticmethod
    def http_request(url, data, http_method, cookie=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url, data, cookies=cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url, data, cookies=cookie)
            else:
                my_logger.info("发送的请求方法错误")
        except Exception as e:
            my_logger.error(f"请求异常:{e}")
            raise e
        return res
