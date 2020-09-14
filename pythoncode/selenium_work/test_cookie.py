# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test_cookie
# Description:  
# Author:       yanghao
# Date:         2020/6/19
# -------------------------------------------------------------------------------
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def test_get_cookie(self):
        time.sleep(10)
        # 一定要在扫码，登录成功之后执行
        cookies = self.driver.get_cookies()
        with open("cookie.json", 'w') as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 处理每个cookie里面是否包含expiry属性
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            # 添加一个dict的cookie信息，把cookie键值对，一个一个的塞入浏览器中
            self.driver.add_cookie(cookie)
        # 如果代码没有问题，但是还是没有成功，多加等待时间
        time.sleep(10)
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10). \
                until(EC.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break
        # expected_conditions.xx 都需要传入的是一个元祖
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "js_upload_file_input")))
        # sendkeys需要使用绝对路径
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(r"C:\Users\SNQU\Desktop\tpl_student(1).xlsx")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "upload_file_name")))
        assert_ele = self.driver.find_element(By.ID, "upload_file_name").text
        assert assert_ele == 'tpl_student(1).xlsx'

    def teardown(self):
        self.driver.quit()
