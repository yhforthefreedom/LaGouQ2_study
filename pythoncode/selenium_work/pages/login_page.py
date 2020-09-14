# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         login_page
# Description:  
# Author:       yanghao
# Date:         2020/6/23
#-------------------------------------------------------------------------------
from pythoncode.selenium_work.common.base_page import *
login_url="http://ecshop.itsoso.cn/user.php"
class LoginPage(BasePage):
    """封装表现层：制作定位器"""
    username_loc = ("name","username") # 用户名输入框
    passwd_loc = ("name","passwd") #密码输入框
    remember_loc = ("id","remember")#记住密码复选框
    submit_loc = ("class name","us_Submit")#立即登录按钮
    """封装操作层：每一个元素的操作写成一个方法"""
    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)
    def input_passwd(self,text):
        self.send_keys(self.passwd_loc,text)
    def click_remember(self):
        if self.is_selected(self.remember_loc):
            pass
        else:
            self.click(self.remember_loc)
    def cilck_submit(self):
        self.click(self.submit_loc)