# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         stack
# Description:  
# Author:       yanghao
# Date:         2020/7/16
# -------------------------------------------------------------------------------
"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""


class Stack:
    """栈"""

    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def push(self, item):
        """加入元素"""
        self.__list.append(item)

    def pop(self):
        """弹出元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def size(self):
        """返回栈的大小"""
        return len(self.__list)
