# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         test_aaa
# Description:  
# Author:       yanghao
# Date:         2020/7/3
#-------------------------------------------------------------------------------
import time
from appium import webdriver
import pytest

class TestWechat:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '6.0.1',
            'appPackage': 'com.tencent.wework',
            'appActivity': 'com.tencent.wework.launch.WwMainActivity',
            "noReset": "true",
            "unicodeKeyboard": "true",
            'resetKeyboard': 'true'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('username,sex,iphone', [("无名","男","14700000009"),("托尼","女","14700000008")])
    def test_add_bbb(self, username, sex, iphone):

            self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
            self.driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("添加成员").instance(0));').click()

            self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()

            self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(
                username)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
            if sex == '女':
                self.driver.find_element_by_xpath("//*[@text='女']").click()
            else:
                self.driver.find_element_by_xpath("//*[@text='男']").click()

            self.driver.find_element_by_xpath("//android.widget.EditText[@text='手机号']").send_keys(iphone)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='保存']").click()
            time.sleep(2)
            toast_text = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
            assert toast_text == "添加成功"
            self.driver.find_element_by_xpath("//*[@text='添加成员']/../../../../android.widget.TextView").click()
            contact_texts = self.driver.find_elements_by_xpath("//android.widget.ListView//android.widget.TextView")
            contact_texts_list = [i.get_attribute("text") for i in contact_texts]
            print(contact_texts_list)
            assert username in contact_texts_list