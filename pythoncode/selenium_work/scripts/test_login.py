# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         test_login
# Description:  
# Author:       yanghao
# Date:         2020/6/23
#-------------------------------------------------------------------------------
from pythoncode.selenium_work.common.base_page import *
from pythoncode.selenium_work.pages.login_page import *

class TestLogin:
    def __init__(self,driver):
        driver = open_brower()#打开浏览器
        self.login = LoginPage(driver)#实例化LoginPage
        self.login.open_url(login_url)
    def test_login(self,username,passwd):
        self.login.input_username(username)
        self.login.input_passwd(passwd)
        self.login.click_submit()