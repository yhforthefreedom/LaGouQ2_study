# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         conftest
# Description:  
# Author:       yanghao
# Date:         2020/6/10
# -------------------------------------------------------------------------------
from typing import List

import pytest
import yaml

from pythoncode.pytest_work.calc_method import *

# 自定义的hook函数，pytest_collection_modifyitems 可以将收集上来的测试用例进行改写，
# 控制用例的执行顺序，自动添加标签，解决测试用例的编码问题
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]):
    # items 就是所有的测试用例列表，item 代表每个测试用例对象
    # items.reverse()翻转执行顺序
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    # if 'add' in item.nodeid:
    #     item.add_marker(pytest.mark.add)
    # elif 'div' in item.nodeid:
    #     item.add_marker(pytest.mark.div)


@pytest.fixture(autouse=True)
def start_calc():
    print("-----开始计算-----")
    calc = Calc()
    yield calc
    print("-----计算结束-----")


def pytest_addoption(parser):
    mygroup = parser.getgroup("yanghao") #group将下面所有的 option都展示在这个group下
    mygroup.addoption("--env",#注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取test数据")
        with open(r"D:\python_work\pythoncode\pytest_work\my_datas\test.yaml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev数据")
        with open(r"D:\python_work\pythoncode\pytest_work\my_datas\dev.yaml") as f:
            datas = yaml.safe_load(f)
    else:
        print("获取st数据")
        with open(r"D:\python_work\pythoncode\pytest_work\my_datas\st.yaml") as f:
            datas = yaml.safe_load(f)
    return datas
