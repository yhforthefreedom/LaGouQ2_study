# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         bubble_sort
# Description:  
# Author:       yanghao
# Date:         2020/7/17
#-------------------------------------------------------------------------------
def bubble_sort(alist):
    """冒泡排序"""
    for j in range(len(list) - 1):
        for i in range(len(alist) - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
