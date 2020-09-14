# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         queue
# Description:  
# Author:       yanghao
# Date:         2020/7/16
# -------------------------------------------------------------------------------
"""
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""


class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def enqueue(self, item):
        """进队列"""
        self.__list.insert(0, item)  # 出队多
        # self.__list.append(item) 入队多

    def dequeue(self):
        """出队列"""
        return self.__list.pop()  # 出队多
        # return self.__list.pop(0) 入队多

    def size(self):
        """返回大小"""
        return len(self.__list)
