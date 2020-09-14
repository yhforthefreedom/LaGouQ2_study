# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         base_page
# Description:  
# Author:       yanghao
# Date:         2020/6/22
# -------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from pythoncode.selenium_work.common.my_log import MyLog
from pythoncode.selenium_work.common.project_path import *

logging = MyLog()
def open_brower(brower):
    if brower == "chrome":
        driver = webdriver.Chrome()
    elif brower == "firefox":
        driver = webdriver.Firefox()
    elif brower == "ie":
        driver = webdriver.Ie()
    else:
        print("请输入正确的浏览器名称，例如chrome，firefox，ie")
        driver = None
    return driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as e:
            logging.info(f"URL获取失败,错误信息为:{e}")

    def close_brower(self):
        self.driver.quit()

    def wait_eleVisible(self, locator, timeout=10, doc=""):
        """等待元素可见"""
        logging.info(f"等待元素 {locator} 可见")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logging.info(f"{doc}:元素 {locator},等待起始时间:{start},等待结束时间:{end},等待时长:{wait_time}")
        except:
            logging.error("等待元素可见异常！！！")
            self.save_screenshot(doc)
            raise

    def wait_elePresence(self, locator, timeout=10, doc=""):
        """等待元素存在"""
        logging.info(f"等待元素 {locator} 可见")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logging.info(f"{doc}:元素{locator},等待起始时间:{start},等待结束时间:{end},等待时长:{wait_time}")
        except:
            logging.error("等待元素可见异常！！！")
            self.save_screenshot(doc)
            raise

    def get_element(self, locator, doc=""):
        """查找元素"""
        logging.info(f"{doc} 查找元素:{locator}")
        try:
            return self.find_element(*locator)
        except:
            logging.error("查找元素失败！！！")
            self.save_screenshot(doc)
            raise

    def get_elements(self, locator, doc=""):
        """查找一组元素"""
        logging.info(f"{doc} 查找元素:{locator}")
        try:
            return self.find_elements(*locator)
        except:
            logging.error("查找元素失败！！！")
            self.save_screenshot(doc)
            raise

    def click_element(self, locator, doc=""):
        """点击操作"""
        element = self.get_element(locator, doc)
        logging.info(f"{doc} 点击元素:{locator}")
        try:
            element.click()
        except:
            logging.info("元素点击操作失败！！！")
            self.save_screenshot(doc)
            raise

    def input_text(self, locator, text, doc=""):
        """输入文本内容操作"""
        element = self.find_element(locator)
        logging.info(f"{doc}:元素:{locator} 输入内容:{text}")
        try:
            element.clear()
            element.send_keys(text)
        except:
            logging.error("元素输入操作失败！！！")
            self.save_screenshot(doc)
            raise

    def get_text(self, locator, doc=""):
        """获取元素的文本内容"""
        element = self.get_element(locator, doc)
        logging.info(f"{doc}:获取元素:{locator}的文本内容")
        try:
            text = element.text
            logging.info(f"元素 {locator} 的文本内容为:{text}")
            return text
        except:
            logging.error("获取元素文本内容失败！！！")
            self.save_screenshot(doc)
            raise

    def get_element_attribute(self, locator, attr, doc=""):
        """获取元素属性"""
        element = self.get_element(locator, doc)
        logging.info(f"{doc}:获取元素:{locator} 的属性:{attr}")
        try:
            element_attr = element.get_attribute(attr)
            logging.info(f"元素 {locator} 的属性 {attr} 值为:{element_attr}")
            return attr
        except:
            logging.error("获取元素的属性失败")
            self.save_screenshot(doc)
            raise

    def is_eleExist(self, locator, timeout=10, doc=""):
        """判断元素是否存在"""
        logging.info(f"{doc} 中是否存在元素 {locator}")
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logging.info(f"{timeout}秒内页面 {doc} 中存在元素:{locator}")
            return True
        except:
            logging.error(f"{timeout}秒内页面 {doc} 中不存在元素:{locator}")
            return False

    def save_screenshot(self, doc):
        """截图操作"""
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒,png
        file_path = screenshot_path + "/{0}_{1}.png".format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(file_path)
            logging.info(f"截屏成功,图片路径为:{file_path}")
        except:
            logging.error("截图失败！！！")
            raise
    def switch_to_window(self, new_window=None):
        """
        切换新窗口
        :param new_window: 新窗口句柄
        :return: 当前窗口句柄
        """
        if new_window is None:
            current_handle = self.driver.window_handles
            try:
                self.driver.switch_to.window(current_handle[-1])
                return current_handle
            except:
                logging.error("切换窗口失败或无新窗口被打开, 无需切换窗口")
                raise
        else:
            self.driver.switch_to.window(new_window)