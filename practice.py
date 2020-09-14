'''map'''
# def f(x):
#     return x*x
# list_a=[1,2,3,4,5,6,7,8,9]
# r=map(f,list_a)
# print(list(r))
# list_a=[1,2,3,4,5,6,7,8,9]
# r=map(lambda x:x**2,list_a)
# print(list(r))
'''reduce'''
# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# print(reduce(fn, [1, 3, 5, 7, 9]))

# print(sorted([36, 5, -12, 9, -21]))
'''filter'''
# a=[96,4,54,6,832,1]
# res=filter(lambda x:x<10,a)
# print(list(res))

# g = (x * x for x in range(10))
# print(next(g))
# print(next(g))

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
# g=odd()
# print(next(g))
# print(next(g))
# print(next(g))


# s = {'唐僧','悟空','悟能','悟净'}
# it = iter(s)
# try:
#     while True:
#         x = next(it)
#         print(x)
# except StopIteration:
#     print('遍历结束')

# s=[1,2,3,4]
# it=iter(s)
#
# for i in range(5):
#     print(next(it))
'''操作excel'''
# import openpyxl
# wb=openpyxl.load_workbook(r'C:\Users\SNQU\Desktop\test1.xlsx')
# sheet=wb['test2']
# print(sheet.rows)
# for row in sheet.rows:
#     for cell in row:
#         print(cell.value,end=',')
#     print()
# for row in sheet.values:
#     print(*row)

'''zip'''
# a1=[1,2,3,4]
# b1=[4,5,6]
# c1=zip(a1,b1)
# print(list(c1))

'''闭包'''
# def func():
#     print('this is a func')
#     def func1():
#         print('this is a func1')
#     return func1
# var=func()
# var()

'''装饰器'''
# def func1(func):#外部闭包函数的参数是被装饰的函数对象
#     def func2():
#         print('aaabbb')
#         return func()#返回了外部函数接受的被装饰函数的调用
#     return func2
# @func1
# def myprint():
#     print('你好，我是print')
# myprint()#func1(myprint)()接收被装饰的函数作为参数，并且还要调用一次

'''爬虫'''
# import requests
# from requests.exceptions import RequestException
# import re
# import json
# def get_one_page(url):
#     try:
#         # 添加头部信息
#         headers = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
#         }
#         response = requests.get(url, headers=headers)
#
#         # 进行状态码判断，是否正确读取到网页
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return None
# def parse_one_page(html):
#     pattern = re.compile('<div.*?win-item-tit clear-fix"><h2.*?f1 w-per-90"><a.*?>(.*?)</a>+<div.*?win-item-info"><d1.*?clear-fix w-per-90 strong-n f1"><dd.*?w-per-18.*?</dd><dd.*?w-per-18">(.*?)</dd>', re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'company': item[0],
#             'phone': item[1],
#
#         }
# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#         f.close()
#
# def main():
#     url = 'http://www.jianshetong.net/companysoso/?provinceid=510000&searchMatch=2&beian=510000_0&anchor=true'
#
#     html = get_one_page(url)
#     print(html)
#     return html
#     # print(html)
#     # parse_one_page(html)
#     # for item in parse_one_page(html):
#     #     print(item)
#     #     write_to_file(item)
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import time,random
# import csv
# for i in range(1,51):
#     url='http://www.jianshetong.net/companysoso/?pageIndex='+str(i)+'&provinceid=120000&searchMatch=2&beian=120000_0&anchor=true'
#     headers = {
#                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#         'Cookie':'Hm_lvt_b326bb923ea83a49902c010bfabee9fc=1585792893,1586224781;UM_distinctid=17152799109673-04b22576b7e35-f313f6d-1fa400-1715279910a363;cbi360=expiretime=1900-01-01&ishistoryvip=0&isvip=2&nickname=68468465&parentuseraccount=13540657075&parentuserid=AAC4488940AC5433926C4BFA23382558D1058EF321FEC665EA58CA29D7F4CB968404EBA2CA58358D&province=%e5%9b%9b%e5%b7%9d&sign=7367f1f843438d29&token=9df2f19f4a5c483582b67e5f8e6c07b9&useraccount=13540657075&userid=AAC4488940AC5433926C4BFA23382558D1058EF321FEC665EA58CA29D7F4CB968404EBA2CA58358D&username=68468465&viplevel=-1&wxlogin=False;cbi360_base=942FCCEC1444F5159128D517DEE39C06FC9D89BB1F5041FF072D158774FC98959C10D449DA3359283515C8D1DBA65724CA1C804120980CC8562EAB48D16734F2FD31DD2A1D41EA3A5D7989171C6D1D46105F6F8CDAE07C3BE11FF6CC3EAF10D58E8CB819C477FC4E070ED4AA1651119B7306AF2605440193471A7411925439675013DE827AB951073FFBEF5EB50270182357CB53B04407124A430921B9B0EA6B42C6E65C767B81906DC13A037EB8321CB7FAE9FAE82E6EB23F35D50A273DF97233456BBFE8E73B69AB3353BF128838B53229D4FF85B353324144EA30D6421DD9;Hm_lvt_a3049665680a2993307c1031331f5843=1585887915,1586224781,1586226827,1586226854;Hm_lpvt_a3049665680a2993307c1031331f5843=1586226854;Hm_lpvt_b326bb923ea83a49902c010bfabee9fc=1586226854'}
#     html= requests.get(url,headers=headers).text
#     time.sleep(random.randint(1,4))
#     soup=BeautifulSoup(html, 'html.parser')
#     li_list=soup.find_all('li')
#     boxes=[]
#     for li in li_list:
#
#         infos=list(li.stripped_strings)
#         if len(infos)>1:
#             box={'公司':infos[1],'联系方式':infos[12]}
#             boxes.append(box)
#     print(boxes)
#     time.sleep(random.randint(3,8))
#     headers=['公司','联系方式']
#     with open('天津津内企业.csv', 'a', encoding='utf-8', newline='') as fp:
#         writer = csv.DictWriter(fp, headers)
#         writer.writeheader()
#         writer.writerows(boxes)
# nums=[2,7,9,9,8,5,2]
# target=7
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         sum=nums[i]+nums[j]
#         if sum == target:
#             print(i,j)
# import time
# start_time=time.time()
# for a in range(0,501):
#     for b in range(0,501):
#         c = 1000 - a - b
#         if a**2 + b**2 ==c**2:
#             print('a={},b={},c={}'.format(a,b,c))
# end_time=time.time()
# print('花费时间:{}'.format(end_time - start_time))
# print("finished")

# def func(n):
#     if n==1:
#         return 1
#     else:
#         return func(n-1)*n
#
# sumlist=[]
# n=int(input(("请输入n的值： ")))
# result=func(n)
# print(result)
# for i in range(1,n+1):
#     sumlist.append(func(i))
# print(sum(sumlist))

# b="[1,2,3]"
#
# a=eval(b)
# print(a,type(a))

# a=[1,2,3,7]
# b=["你","我","他",9]
# c={"a1":4,"b2":5}
# ab=zip(a,b,c)
# print(list(ab))

# a=[1,2,3]
# print(*a)

# dic={"name":"zhaozhao","password":"123456"}
#
# def dic_fun(name,password):
#     print(name)
#     print(password)
#
# dic_fun(**dic)

# import time
# start_time=time.time()
# list1=[1,2,3,4,5,6,7,8,9,24,345,24,456,756,234,645]
# list2=['a','b','c','你','我','他']
# list3=[*list1,*list2]
# print(list3)
# end_time=time.time()
# print('花费时间:{}'.format(end_time - start_time))

# import os
# dict = os.path.dirname(__file__)
# print(__file__)

# from appium import webdriver
import time
import pytest
from hamcrest import *

# desired_caps = {
#             'platformName': 'Android',
#             'deviceName': 'emulator-5554',
#             'platformVersion': '6.0.1',
#             'appPackage': 'com.tencent.wework',
#             'appActivity': 'com.tencent.wework.launch.WwMainActivity',
#             "noReset": "true",
#             "unicodeKeyboard": "true",
#             'resetKeyboard': 'true'
#             }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(15)
# ele1=driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/gud']/android.widget.RelativeLayout[2]").click()
# ele2=driver.find_element_by_xpath("//*[@text='添加成员']").click()
# ele3=driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
# ele4=driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/e43']//android.widget.EditText").send_keys("啥是gay")
# ele5=driver.find_element_by_xpath("//android.widget.EditText[@text='手机号']").send_keys("13006423371")
#
# ele6=driver.find_element_by_xpath("//*[@text='保存']").click()
# ele7=driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
# class TestDemo:
#     def setup(self):
#         desired_caps = {
#         "deviceName": "mumu",
#         "platformVersion": "6.0.1",
#         "appPackage": "com.xueqiu.android",
#         "appActivity": "com.xueqiu.android.common.MainActivity",
#         "platformName": "Android",
#         "autoAcceptAlerts": "true",
#         "noReset": "true"
#         }
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#         self.driver.implicitly_wait(15)
#
#     def test_search(self):
#         el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
#         el1.click()
#         el2 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
#         el2.click()
#
#         el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
#         el3.send_keys("阿里巴巴")
#         el4=self.driver.find_element_by_xpath("//*[@text='阿里巴巴' and @class='android.widget.TextView']")
#         el4.click()
#         el5=float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
#     def teardown(self):
#
#         self.driver.quit()


import time, datetime, os, sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
images_dir = r_config(conf_dir, "image", "img_path")
logger = Log(log_dir)
# 封装基本函数 - 执行日志、 异常处理、 截图
class BasePage:
    def __init__(self, driver):
        self.driver = driver
# 截图
    def save_pictuer(self, doc):
        filePath = images_dir + '{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logger.info('{0}截图成功，图片路径为: {0}'.format(doc, filePath))
        except:
            logger.info('{0}截图 失败'.format(doc))
# 等待页面元素可见
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info('{0},等待页面元素:{1}:可见，共耗时{2}s '.format(doc, locator, wait_time))
        except:
            logger.info('{0},等待页面元素:{1} 失败！！！'.format(doc, locator))
            self.save_pictuer(doc)
# 等待页面元素存在
    def wait_elePresence(self):
        pass
# 查找页面元素
    def get_element(self, locator, doc=''):

        logger.info('{0},查找页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.driver.find_element(*locator)
        except:
            logger.info('{0},查找页面元素:{1} 失败！！！'.format(doc, locator))
            raise
# 点击页面元素
    def click_element(self, locator, doc=''):
        logger.info('{0},点击页面元素:{1}'.format(doc, locator))
        try:
            self.get_element(locator, doc).click()
        except:
            logger.info('点击页面元素:{0},失败！！！'.format(locator))
            raise
# 输入操作
    def input_element(self, locator, key, doc=''):
        logger.info('{0},页面元素:{1} 输入值 {2}'.format(doc, locator, key))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).send_keys(key)
        except:
            logger.info('{0},页面元素输入失败！！！'.format(doc))
            raise
# 获取文本
    def get_element_text(self, locator, doc=''):
        logger.info('{0},获取页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).text
        except:
            logger.info('{0},页面元素的文本获取失败！！！'.format(doc))
            raise
# 获取页面元素属性
    def get_element_attribute(self, attr, locator, doc=''):
        logger.info('{0},获取页面元素属性:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).get_attribute(attr)
        except:
            logger.info('{0},页面元素的属性获取 失败！！！'.format(doc))
            raise
# alter 处理
    def alter_action(self):
        pass
# iframe 切换
    def switch_iframe(self):
        pass
# windows 切换
    def switch_window(self):
        pass
# 上传操作
    def upload_file(self):
        pass

