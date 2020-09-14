# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         deque
# Description:  
# Author:       yanghao
# Date:         2020/7/16
# -------------------------------------------------------------------------------
"""
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
"""


class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def add_front(self, item):
        """在队头添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.__list.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        return self.__list.pop()

    def size(self):
        """返回队列大小"""
        return len(self.__list)
