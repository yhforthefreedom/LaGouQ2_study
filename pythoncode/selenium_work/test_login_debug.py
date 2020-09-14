# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test_login_debug
# Description:  
# Author:       yanghao
# Date:         2020/6/19
# -------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_debug_login(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
